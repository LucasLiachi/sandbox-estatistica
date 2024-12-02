import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from datetime import datetime
import os

def get_deputies_data():
    url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
    try:
        response = requests.get(url)
        return response.json()['dados']
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def update_database(data):
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'media-deputado-camara.db')
        conn = sqlite3.connect(db_path)
        df = pd.DataFrame(data)
        df['ultima_atualizacao'] = datetime.now()
        df.to_sql('deputados', conn, if_exists='replace', index=False)
        conn.close()
        return True
    except Exception as e:
        print(f"Error updating database: {e}")
        return False

def analyze_from_database():
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'media-deputado-camara.db')
        conn = sqlite3.connect(db_path)
        
        # Read data from database
        query = """
        SELECT siglaUf, siglaPartido, COUNT(*) as total_deputies,
               (SELECT COUNT(DISTINCT siglaPartido) 
                FROM deputados d2 
                WHERE d2.siglaUf = d1.siglaUf) as unique_parties
        FROM deputados d1
        GROUP BY siglaUf, siglaPartido
        """
        df = pd.read_sql_query(query, conn)
        
        # Analysis by state
        state_analysis = df.groupby('siglaUf').agg({
            'total_deputies': 'sum',
            'unique_parties': 'first'
        })
        state_analysis['avg_deputies_per_party'] = state_analysis['total_deputies'] / state_analysis['unique_parties']
        
        # Create visualizations
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Deputies per Party by State
        plt.subplot(2, 1, 1)
        sns.barplot(x=state_analysis.index, 
                   y=state_analysis['avg_deputies_per_party'])
        plt.title('Average Deputies per Party by State')
        plt.xticks(rotation=45)
        
        # Plot 2: Party Distribution
        plt.subplot(2, 1, 2)
        party_counts = df.groupby('siglaPartido')['total_deputies'].sum()
        sns.barplot(x=party_counts.index, y=party_counts.values)
        plt.title('Number of Deputies by Party')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.show()
        
        conn.close()
        return state_analysis
        
    except Exception as e:
        print(f"Error analyzing database: {e}")
        return None

if __name__ == "__main__":
    # Update database with fresh data
    data = get_deputies_data()
    if data and update_database(data):
        print("Database updated successfully")
        
    # Perform analysis
    result = analyze_from_database()
    if result is not None:
        print("\nState Analysis (sorted by average deputies per party):")
        print(result.sort_values('avg_deputies_per_party', ascending=False))
