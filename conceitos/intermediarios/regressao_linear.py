"""
Módulo de Regressão Linear.

Este módulo implementa regressão linear simples e múltipla,
incluindo análise de resíduos e métricas de avaliação.

Author: Lucas
Date: 2025
"""

import numpy as np
import pandas as pd
from typing import Tuple, Union, Optional
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RegressaoLinear:
    """
    Implementa análise de regressão linear simples e múltipla.
    
    Attributes:
        model: Modelo de regressão linear
        is_fitted (bool): Indica se o modelo foi treinado
        coef_ (np.ndarray): Coeficientes do modelo após o treino
        intercept_ (float): Intercepto do modelo após o treino
    """
    
    def __init__(self):
        """Inicializa o modelo de regressão linear."""
        self.model = LinearRegression()
        self.is_fitted = False
        self.coef_ = None
        self.intercept_ = None
    
    def validate_input(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Valida os dados de entrada para a regressão.

        Args:
            X: Array com variáveis independentes
            y: Array com variável dependente

        Raises:
            ValueError: Se os dados não atenderem aos critérios
        """
        if not isinstance(X, (np.ndarray, pd.DataFrame)):
            raise ValueError("X deve ser um array numpy ou DataFrame")
        
        if not isinstance(y, (np.ndarray, pd.Series)):
            raise ValueError("y deve ser um array numpy ou Series")
            
        if X.shape[0] != y.shape[0]:
            raise ValueError("X e y devem ter o mesmo número de observações")
            
        if np.isnan(X).any() or np.isnan(y).any():
            raise ValueError("Os dados não podem conter valores ausentes")
    
    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Treina o modelo de regressão linear.

        Args:
            X: Array com variáveis independentes
            y: Array com variável dependente
        """
        try:
            self.validate_input(X, y)
            self.model.fit(X, y)
            self.is_fitted = True
            self.coef_ = self.model.coef_
            self.intercept_ = self.model.intercept_
            logger.info("Modelo treinado com sucesso")
        except Exception as e:
            logger.error(f"Erro ao treinar modelo: {str(e)}")
            raise
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Realiza previsões com o modelo treinado.

        Args:
            X: Array com variáveis independentes

        Returns:
            Array com previsões

        Raises:
            ValueError: Se o modelo não foi treinado
        """
        if not self.is_fitted:
            raise ValueError("O modelo precisa ser treinado antes de fazer previsões")
        return self.model.predict(X)
    
    def evaluate(self, X: np.ndarray, y: np.ndarray) -> dict:
        """
        Avalia o modelo usando várias métricas.

        Args:
            X: Array com variáveis independentes
            y: Array com valores reais

        Returns:
            Dicionário com métricas de avaliação
        """
        y_pred = self.predict(X)
        return {
            'r2': r2_score(y, y_pred),
            'mse': mean_squared_error(y, y_pred),
            'rmse': np.sqrt(mean_squared_error(y, y_pred))
        }
    
    def plot_regression(self, X: np.ndarray, y: np.ndarray, 
                       feature_names: Optional[list] = None) -> None:
        """
        Plota os resultados da regressão.

        Args:
            X: Array com variáveis independentes
            y: Array com valores reais
            feature_names: Lista opcional com nomes das features
        """
        if X.shape[1] == 1:  # Regressão simples
            plt.figure(figsize=(10, 6))
            plt.scatter(X, y, alpha=0.5)
            plt.plot(X, self.predict(X), color='red', linewidth=2)
            plt.xlabel(feature_names[0] if feature_names else 'X')
            plt.ylabel('y')
            plt.title('Regressão Linear Simples')
            plt.show()
            
            # Plot de resíduos
            residuos = y - self.predict(X)
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=self.predict(X).ravel(), y=residuos)
            plt.axhline(y=0, color='r', linestyle='--')
            plt.xlabel('Valores Previstos')
            plt.ylabel('Resíduos')
            plt.title('Análise de Resíduos')
            plt.show()

def criar_dados_exemplo(n_samples: int = 100, 
                       n_features: int = 1, 
                       noise: float = 1.0, 
                       random_state: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    """
    Cria dados sintéticos para exemplo de regressão.

    Args:
        n_samples: Número de amostras
        n_features: Número de features
        noise: Nível de ruído nos dados
        random_state: Semente aleatória

    Returns:
        Tuple com arrays X e y
    """
    np.random.seed(random_state)
    X = np.random.rand(n_samples, n_features) * 10
    coef = np.random.rand(n_features)
    y = np.dot(X, coef) + np.random.randn(n_samples) * noise
    return X, y

if __name__ == "__main__":
    # Exemplo de uso
    try:
        # Criar dados de exemplo
        X, y = criar_dados_exemplo(n_samples=100, n_features=1)
        
        # Dividir em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Criar e treinar modelo
        modelo = RegressaoLinear()
        modelo.fit(X_train, y_train)
        
        # Avaliar modelo
        metricas = modelo.evaluate(X_test, y_test)
        logger.info("\nMétricas de Avaliação:")
        for metrica, valor in metricas.items():
            logger.info(f"{metrica}: {valor:.4f}")
        
        # Plotar resultados
        modelo.plot_regression(X, y, ['Feature 1'])
        
    except Exception as e:
        logger.error(f"Erro na execução: {str(e)}")