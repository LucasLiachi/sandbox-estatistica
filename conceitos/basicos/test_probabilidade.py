"""
Testes unitários para o módulo de probabilidade.
"""

import unittest
import numpy as np
from conceitos.basicos.Probabilidade import calcular_intervalo_confianca, validar_dados

class TestProbabilidade(unittest.TestCase):
    def setUp(self):
        """Define dados de teste para uso nos casos de teste."""
        self.notas_validas = [82, 64, 64, 79, 64, 76, 52, 61, 85]
        self.nivel_confianca = 0.95

    def test_validar_dados_validos(self):
        """Testa a validação de dados com entrada válida."""
        try:
            validar_dados(self.notas_validas, self.nivel_confianca)
        except ValueError:
            self.fail("validar_dados() levantou ValueError inesperadamente!")

    def test_validar_dados_lista_vazia(self):
        """Testa a validação com lista vazia."""
        with self.assertRaises(ValueError):
            validar_dados([], self.nivel_confianca)

    def test_validar_dados_notas_invalidas(self):
        """Testa a validação com notas não numéricas."""
        with self.assertRaises(ValueError):
            validar_dados([1, 2, "3"], self.nivel_confianca)

    def test_validar_nivel_confianca_invalido(self):
        """Testa a validação com nível de confiança inválido."""
        with self.assertRaises(ValueError):
            validar_dados(self.notas_validas, 1.5)

    def test_calculo_intervalo_confianca(self):
        """Testa o cálculo do intervalo de confiança com valores conhecidos."""
        lim_inferior, lim_superior = calcular_intervalo_confianca(self.notas_validas)
        
        # Verifica se os limites são números
        self.assertTrue(isinstance(lim_inferior, float))
        self.assertTrue(isinstance(lim_superior, float))
        
        # Verifica se o intervalo é válido
        self.assertLess(lim_inferior, lim_superior)
        
        # Verifica se a média está dentro do intervalo
        media = np.mean(self.notas_validas)
        self.assertTrue(lim_inferior <= media <= lim_superior)

    def test_intervalo_confianca_amostra_pequena(self):
        """Testa o cálculo com amostra pequena."""
        notas_pequenas = [1, 2, 3]
        lim_inferior, lim_superior = calcular_intervalo_confianca(notas_pequenas)
        
        # Verifica se o intervalo é maior para amostras pequenas
        amplitude = lim_superior - lim_inferior
        self.assertGreater(amplitude, 0)

if __name__ == '__main__':
    unittest.main()