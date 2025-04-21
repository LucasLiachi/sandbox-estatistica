"""
Testes unitários para o módulo de Regressão Linear.
"""

import unittest
import numpy as np
from conceitos.intermediarios.regressao_linear import RegressaoLinear, criar_dados_exemplo

class TestRegressaoLinear(unittest.TestCase):
    def setUp(self):
        """Define dados de teste para uso nos casos de teste."""
        self.modelo = RegressaoLinear()
        self.X, self.y = criar_dados_exemplo(n_samples=50, n_features=1, random_state=42)
        
    def test_validate_input_valid(self):
        """Testa a validação com dados válidos."""
        try:
            self.modelo.validate_input(self.X, self.y)
        except ValueError:
            self.fail("validate_input() levantou ValueError inesperadamente!")

    def test_validate_input_invalid_type(self):
        """Testa a validação com tipo de dados inválido."""
        with self.assertRaises(ValueError):
            self.modelo.validate_input([1, 2, 3], self.y)  # Lista ao invés de array

    def test_validate_input_shape_mismatch(self):
        """Testa a validação com shapes incompatíveis."""
        with self.assertRaises(ValueError):
            self.modelo.validate_input(self.X, self.y[:-1])  # Remove último elemento de y

    def test_validate_input_nan_values(self):
        """Testa a validação com valores NaN."""
        X_with_nan = self.X.copy()
        X_with_nan[0,0] = np.nan
        with self.assertRaises(ValueError):
            self.modelo.validate_input(X_with_nan, self.y)

    def test_fit_predict(self):
        """Testa o treino e previsão do modelo."""
        self.modelo.fit(self.X, self.y)
        
        # Verifica se o modelo foi marcado como treinado
        self.assertTrue(self.modelo.is_fitted)
        
        # Verifica se os atributos foram definidos
        self.assertIsNotNone(self.modelo.coef_)
        self.assertIsNotNone(self.modelo.intercept_)
        
        # Testa previsões
        y_pred = self.modelo.predict(self.X)
        self.assertEqual(y_pred.shape, self.y.shape)

    def test_evaluate(self):
        """Testa a avaliação do modelo."""
        self.modelo.fit(self.X, self.y)
        metrics = self.modelo.evaluate(self.X, self.y)
        
        # Verifica se todas as métricas foram calculadas
        self.assertIn('r2', metrics)
        self.assertIn('mse', metrics)
        self.assertIn('rmse', metrics)
        
        # Verifica se as métricas são válidas
        self.assertTrue(0 <= metrics['r2'] <= 1)  # R² deve estar entre 0 e 1
        self.assertGreater(metrics['mse'], 0)     # MSE deve ser positivo
        self.assertGreater(metrics['rmse'], 0)    # RMSE deve ser positivo

    def test_predict_without_fit(self):
        """Testa previsão sem treinar o modelo."""
        with self.assertRaises(ValueError):
            self.modelo.predict(self.X)

    def test_criar_dados_exemplo(self):
        """Testa a função de criação de dados de exemplo."""
        X, y = criar_dados_exemplo(n_samples=100, n_features=2)
        
        # Verifica as dimensões
        self.assertEqual(X.shape[0], 100)
        self.assertEqual(X.shape[1], 2)
        self.assertEqual(y.shape[0], 100)
        
        # Verifica se não há valores NaN
        self.assertFalse(np.isnan(X).any())
        self.assertFalse(np.isnan(y).any())

if __name__ == '__main__':
    unittest.main()