import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from datetime import datetime
import sqlite3
import logging
from pathlib import Path
import json
from functools import lru_cache

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_resilient_session():
    """Configure session with retry mechanism"""
    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

@lru_cache(maxsize=32)
def get_cached_data(url, params=None):
    """Cache API responses to reduce server load"""
    session = setup_resilient_session()
    try:
        response = session.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Error fetching data from {url}: {str(e)}")
        return None

def setup_db():
    conn = sqlite3.connect('projetos/PJ-econometria/projeto-econometria.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS economic_data (
        ano INTEGER PRIMARY KEY,
        pib REAL,
        empregos REAL,
        importacoes REAL,
        exportacoes REAL,
        data_atualizacao TIMESTAMP
    )
    ''')
    conn.commit()
    return conn

def save_economic_data(data_dict, conn):
    cursor = conn.cursor()
    current_time = datetime.now()
    for ano, values in data_dict.items():
        cursor.execute('''
        INSERT OR REPLACE INTO economic_data
        (ano, pib, empregos, importacoes, exportacoes, data_atualizacao)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (ano, values['pib'], values['empregos'],
              values['importacoes'], values['exportacoes'], current_time))
    conn.commit()

def process_agregados_data(data):
    pib_data = {}
    for item in data:
        for result in item['resultados']:
            for serie in result['series']:
                for periodo, valor in serie['serie'].items():
                    try:
                        pib_data[int(periodo)] = float(valor)
                    except (ValueError, TypeError):
                        continue
    if not pib_data:
        raise Exception("No PIB data retrieved from API")
    return pib_data

def process_sidra_data(data):
    pib_data = {}
    for item in data:
        try:
            periodo = int(item['D1C'])
            valor = float(item['V'])
            pib_data[periodo] = valor
        except (ValueError, TypeError):
            continue
    if not pib_data:
        raise Exception("No PIB data retrieved from API")
    return pib_data

def process_pib_data(data):
    """Process PIB data from IBGE API response"""
    try:
        pib_data = {}
        for item in data:
            for result in item['resultados']:
                for serie in result['series']:
                    for periodo, valor in serie['serie'].items():
                        try:
                            # Convert string values to appropriate numeric types
                            ano = int(periodo)
                            # Convert string to float and handle different number formats
                            valor_str = str(valor).replace(',', '.')
                            pib = float(valor_str)
                            pib_data[ano] = pib
                        except (ValueError, TypeError) as e:
                            logging.warning(f"Error processing PIB value for period {periodo}: {e}")
                            continue
        
        if not pib_data:
            raise ValueError("No valid PIB data found in API response")
        
        # Validate data range
        expected_years = set(range(2012, 2021))
        missing_years = expected_years - set(pib_data.keys())
        if missing_years:
            logging.warning(f"Missing PIB data for years: {missing_years}")
        
        return pib_data
    
    except Exception as e:
        logging.error(f"Error processing PIB data: {e}")
        return None

def get_pib_data():
    """Get PIB data from IBGE API with improved error handling"""
    try:
        url = "https://servicodados.ibge.gov.br/api/v3/agregados/6784/periodos/2012|2013|2014|2015|2016|2017|2018|2019|2020/variaveis/37?localidades=N1[all]"
        session = setup_resilient_session()
        
        response = session.get(url, timeout=15)
        response.raise_for_status()
        
        data = response.json()
        if not data:
            raise ValueError("Empty response from IBGE API")
        
        pib_data = process_pib_data(data)
        if not pib_data:
            raise ValueError("Failed to process PIB data")
        
        logging.info(f"Successfully retrieved PIB data for {len(pib_data)} years")
        return pib_data
        
    except requests.RequestException as e:
        logging.error(f"Error accessing IBGE API: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error getting PIB data: {e}")
        return None

def process_employment_data(data, source):
    employment_data = {}
    if source == 'ibge':
        for item in data:
            ano = int(item['periodo'])
            valor = float(item['serie']['2006']['valor'])
            employment_data[ano] = valor
    elif source == 'bcb':
        for item in data:
            try:
                ano = int(item['data'][:4])
                valor = float(item['valor'])
                employment_data[ano] = valor
            except (ValueError, TypeError):
                continue
    if not employment_data:
        raise Exception("No employment data retrieved from API")
    return employment_data

def get_employment_data():
    """Get employment data with alternative sources"""
    urls = [
        "https://servicodados.ibge.gov.br/api/v1/pesquisas/6381/periodos/2012|2013|2014|2015|2016|2017|2018|2019|2020/indicadores/4099",
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.24369/dados?formato=json"
    ]
    
    for url in urls:
        data = get_cached_data(url)
        if data:
            try:
                return process_employment_data(data, 'ibge' if 'ibge' in url else 'bcb')
            except Exception as e:
                logging.error(f"Error processing employment data: {str(e)}")
                continue
    
    logging.error("All employment data sources failed")
    return None

def process_trade_data(data, source):
    trade_data = {}
    if source == 'comex':
        for item in data:
            ano = int(item['ano'])
            exportacoes = float(item['exportacoes']['valor'])
            importacoes = float(item['importacoes']['valor'])
            trade_data[ano] = {'exportacoes': exportacoes, 'importacoes': importacoes}
    elif source == 'bcb':
        for item in data:
            try:
                ano = int(item['data'][:4])
                valor = float(item['valor'])
                if ano not in trade_data:
                    trade_data[ano] = {'exportacoes': 0, 'importacoes': 0}
                trade_data[ano]['exportacoes'] += valor if 'exportacao' in item['id'] else 0
                trade_data[ano]['importacoes'] += valor if 'importacao' in item['id'] else 0
            except (ValueError, TypeError):
                continue
    if not trade_data:
        raise Exception("No trade data retrieved from API")
    return trade_data

def get_trade_data():
    """Get trade data with alternative sources"""
    urls = [
        ("https://api-comex-estatisticas.siscomex.gov.br/api/v1/comercio-exterior/exportacao-importacao/totais-mensais",
         {'ano': '2012,2013,2014,2015,2016,2017,2018,2019,2020'}),
        ("https://api.bcb.gov.br/dados/serie/bcdata.sgs.22699/dados?formato=json", None)
    ]
    
    for url, params in urls:
        data = get_cached_data(url, params)
        if data:
            try:
                return process_trade_data(data, 'comex' if 'comex' in url else 'bcb')
            except Exception as e:
                logging.error(f"Error processing trade data: {str(e)}")
                continue
    
    logging.error("All trade data sources failed")
    return None

def get_economic_data():
    conn = setup_db()
    pib_data = get_pib_data()
    employment_data = get_employment_data()
    trade_data = get_trade_data()

    if not all([pib_data, employment_data, trade_data]):
        print("Error: Could not retrieve all required data")
        return None

    combined_data = {}
    for year in range(2012, 2021):
        combined_data[year] = {
            'pib': pib_data.get(year, 0),
            'empregos': employment_data.get(year, 0),
            'importacoes': trade_data.get(year, {}).get('importacoes', 0),
            'exportacoes': trade_data.get(year, {}).get('exportacoes', 0)
        }

    save_economic_data(combined_data, conn)
    return combined_data

def analyze_economic_data(df):
    """Perform economic data analysis"""
    if df.empty:
        print("Error: No data available for analysis")
        return

    # Calculate PIB per capita
    df['PIB_per_capita'] = df['pib'] / 210

    # Prepare data for regression
    X = df[['pib', 'empregos', 'exportacoes', 'importacoes']]
    y = df['PIB_per_capita']

    # Fit model
    modelo = LinearRegression()
    modelo.fit(X, y)
    r2 = modelo.score(X, y)

    # Print results
    print("\nAnálise de Regressão Multivariada:")
    print("-" * 40)
    for name, coef in zip(['PIB', 'Empregos', 'Exportacoes', 'Importacoes'], modelo.coef_):
        print(f"Coeficiente {name}: {coef:.4f}")
    print(f"\nR² do modelo: {r2:.4f}")
    print("-" * 40)

    # Visualizations
    plot_results(df, X, y, modelo)
    plot_correlation_matrix(df)

def plot_results(df, X, y, modelo):
    plt.figure(figsize=(10, 6))
    plt.scatter(df.index, y, color='blue', label='Dados reais')
    plt.plot(df.index, modelo.predict(X), color='red', label='Previsão do modelo')
    plt.xlabel('Ano')
    plt.ylabel('PIB per capita')
    plt.title('PIB per capita: Dados Reais vs. Previsão do Modelo')
    plt.legend()
    plt.show()

def plot_correlation_matrix(df):
    plt.figure(figsize=(10, 8))
    correlation_matrix = df[['pib', 'empregos', 'exportacoes', 'importacoes']].corr()
    plt.imshow(correlation_matrix, cmap='coolwarm', aspect='auto')
    plt.colorbar()
    plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
    plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
    plt.title('Matriz de Correlação')
    plt.tight_layout()
    plt.show()

def main():
    try:
        economic_data = get_economic_data()
        if economic_data:
            df = pd.DataFrame.from_dict(economic_data, orient='index')
            analyze_economic_data(df)
        else:
            logging.error("Failed to collect economic data")
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()