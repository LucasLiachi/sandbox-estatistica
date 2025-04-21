"""
Testes unitários para o módulo ANOVA.
"""

import unittest
import numpy as np
import pandas as pd
from conceitos.intermediarios.ANOVA import calculate_anova, validate_data_groups

class TestANOVA(unittest.TestCase):
    def setUp(self):
        """Define dados de teste para uso nos casos de teste."""
        self.valid_data = {
            'grupo1': [1, 2, 3, 4, 5],
            'grupo2': [2, 3, 4, 5, 6],
            'grupo3': [3, 4, 5, 6, 7]
        }
        
    def test_validate_data_groups_valid(self):
        """Testa a validação com dados válidos."""
        try:
            validate_data_groups(self.valid_data)
        except ValueError:
            self.fail("validate_data_groups() levantou ValueError inesperadamente!")

    def test_validate_data_groups_invalid_type(self):
        """Testa a validação com tipo de dados inválido."""
        with self.assertRaises(ValueError):
            validate_data_groups([1, 2, 3])  # Lista ao invés de dicionário

    def test_validate_data_groups_empty_group(self):
        """Testa a validação com grupo vazio."""
        invalid_data = {
            'grupo1': [1, 2, 3],
            'grupo2': []
        }
        with self.assertRaises(ValueError):
            validate_data_groups(invalid_data)

    def test_validate_data_groups_non_numeric(self):
        """Testa a validação com valores não numéricos."""
        invalid_data = {
            'grupo1': [1, 2, '3'],
            'grupo2': [4, 5, 6]
        }
        with self.assertRaises(ValueError):
            validate_data_groups(invalid_data)

    def test_anova_calculation(self):
        """Testa o cálculo da ANOVA com valores conhecidos."""
        result = calculate_anova(self.valid_data)
        
        # Verifica se o resultado é um DataFrame
        self.assertIsInstance(result, pd.DataFrame)
        
        # Verifica as colunas necessárias
        required_columns = [
            'Fonte de Variação',
            'Soma de Quadrados (SQ)',
            'Graus de Liberdade (df)',
            'Quadrados Médios (QM)',
            'Valor F'
        ]
        for col in required_columns:
            self.assertIn(col, result.columns)
        
        # Verifica os graus de liberdade
        df_values = result['Graus de Liberdade (df)'].tolist()
        self.assertEqual(df_values[0], len(self.valid_data) - 1)  # gl entre grupos
        self.assertEqual(df_values[1], len(self.valid_data) * 5 - len(self.valid_data))  # gl dentro dos grupos

    def test_anova_equal_groups(self):
        """Testa ANOVA com grupos idênticos (deve resultar em F próximo de 0)."""
        equal_data = {
            'grupo1': [1, 1, 1],
            'grupo2': [1, 1, 1],
            'grupo3': [1, 1, 1]
        }
        result = calculate_anova(equal_data)
        f_value = float(result.loc[result['Fonte de Variação'] == 'Entre Grupos', 'Valor F'].values[0])
        self.assertAlmostEqual(f_value, 0, places=10)

    def test_anova_different_groups(self):
        """Testa ANOVA com grupos muito diferentes (deve resultar em F grande)."""
        different_data = {
            'grupo1': [1, 1, 1],
            'grupo2': [10, 10, 10],
            'grupo3': [20, 20, 20]
        }
        result = calculate_anova(different_data)
        f_value = float(result.loc[result['Fonte de Variação'] == 'Entre Grupos', 'Valor F'].values[0])
        self.assertGreater(f_value, 100)  # F deve ser grande para grupos muito diferentes

if __name__ == '__main__':
    unittest.main()