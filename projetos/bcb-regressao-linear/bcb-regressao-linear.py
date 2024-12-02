import numpy as np
import pandas as pd
import sqlite3
import requests
import os
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from typing import Tuple, Dict
import matplotlib
matplotlib.use('Agg')  # Add this line at the top after import matplotlib

class BCBAnalyzer:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
        self.df = None
        self.model = None

    def fetch_and_save_data(self) -> None:
        """Fetch data from API and save to database"""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            
            with sqlite3.connect(self.db_path) as conn:
                df = pd.DataFrame(data)
                df.to_sql('bcb_series', conn, if_exists='replace', index=False)
        except Exception as e:
            print(f"Error in data fetch/save: {e}")
            raise

    def load_data(self) -> None:
        """Load and prepare data from database"""
        with sqlite3.connect(self.db_path) as conn:
            self.df = pd.read_sql_query("SELECT * FROM bcb_series", conn)
        # Fix date parsing for Brazilian format
        self.df['data'] = pd.to_datetime(self.df['data'], format='%d/%m/%Y')
        self.df['valor'] = pd.to_numeric(self.df['valor'], errors='coerce')

    def perform_analysis(self) -> Dict:
        """Perform statistical analysis and regression"""
        X = np.arange(len(self.df)).reshape(-1, 1)
        y = self.df['valor'].values

        self.model = LinearRegression()
        self.model.fit(X, y)
        y_pred = self.model.predict(X)

        return {
            'mean': np.mean(y),
            'std': np.std(y),
            'slope': self.model.coef_[0],
            'intercept': self.model.intercept_,
            'X': X,
            'y': y,
            'y_pred': y_pred
        }

    def plot_results(self, results: Dict) -> None:
        """Create visualization plots and save to files"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        # Time series plot
        ax1.plot(self.df['data'], self.df['valor'], 'b-', label='Time Series')
        ax1.set_title('BCB Time Series Data')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Value')
        ax1.legend()

        # Regression plot
        ax2.scatter(results['X'], results['y'], c='blue', label='Actual Data')
        ax2.plot(results['X'], results['y_pred'], 'r-', label='Regression Line')
        ax2.set_title('Linear Regression Analysis')
        ax2.set_xlabel('Time Index')
        ax2.set_ylabel('Value')
        ax2.legend()

        plt.tight_layout()
        # Save plots in Analises/bcb-regressao-linear directory
        output_path = 'Analises/bcb-regressao-linear/bcb_analysis_plots.png'
        plt.savefig(output_path)
        plt.close()

def main():
    analyzer = BCBAnalyzer('Analises/bcb-regressao-linear/bcb_data.db')
    
    try:
        analyzer.fetch_and_save_data()
        analyzer.load_data()
        results = analyzer.perform_analysis()

        print("\nStatistical Analysis:")
        print(f"Mean: {results['mean']:.2f}")
        print(f"Standard Deviation: {results['std']:.2f}")
        print(f"\nRegression Results:")
        print(f"Slope: {results['slope']:.4f}")
        print(f"Intercept: {results['intercept']:.4f}")

        analyzer.plot_results(results)

    except Exception as e:
        print(f"Analysis failed: {e}")

if __name__ == "__main__":
    main()


