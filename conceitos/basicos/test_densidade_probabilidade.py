"""
Testes unitários para o módulo de densidade de probabilidade.
"""

import unittest
import numpy as np
from conceitos.basicos.densidade_de_probabilidade import (
    DistribuicaoProbabilidade,
    PDFValidationError,
    DISTRIBUICOES_EXEMPLO
)

class TestDistribuicaoProbabilidade(unittest.TestCase):
    def setUp(self):
        """Define dados de teste para uso nos casos de teste."""
        # Distribuição exponencial para testes
        self.dist_exp = DistribuicaoProbabilidade(
            DISTRIBUICOES_EXEMPLO['exponencial']['funcao'],
            DISTRIBUICOES_EXEMPLO['exponencial']['var'],
            DISTRIBUICOES_EXEMPLO['exponencial']['dominio']
        )

    def test_validar_distribuicao_valida(self):
        """Testa a validação com uma distribuição válida."""
        try:
            dist = DistribuicaoProbabilidade('exp(-x)', 'x', (0, float('inf')))
        except PDFValidationError:
            self.fail("DistribuicaoProbabilidade() levantou erro inesperadamente!")

    def test_validar_distribuicao_invalida(self):
        """Testa a validação com uma distribuição inválida (não normalizada)."""
        with self.assertRaises(PDFValidationError):
            DistribuicaoProbabilidade('2*exp(-x)', 'x', (0, float('inf')))

    def test_validar_distribuicao_negativa(self):
        """Testa a validação com uma distribuição que assume valores negativos."""
        with self.assertRaises(PDFValidationError):
            DistribuicaoProbabilidade('-exp(-x)', 'x', (0, float('inf')))

    def test_calcular_probabilidade(self):
        """Testa o cálculo de probabilidade em intervalos."""
        # Para distribuição exponencial com λ=2, P(0 ≤ X ≤ 1) = 1 - e^(-2)
        prob = self.dist_exp.calcular_probabilidade((0, 1))
        esperado = 1 - np.exp(-2)
        self.assertAlmostEqual(prob, esperado, places=6)

    def test_calcular_media(self):
        """Testa o cálculo da média."""
        # Para distribuição exponencial com λ=2, média = 1/λ = 1/2
        media = self.dist_exp.calcular_media()
        self.assertAlmostEqual(media, 0.5, places=6)

    def test_calcular_variancia(self):
        """Testa o cálculo da variância."""
        # Para distribuição exponencial com λ=2, variância = 1/λ² = 1/4
        variancia = self.dist_exp.calcular_variancia()
        self.assertAlmostEqual(variancia, 0.25, places=6)

    def test_distribuicao_triangular(self):
        """Testa cálculos com a distribuição triangular."""
        dist_tri = DistribuicaoProbabilidade(
            DISTRIBUICOES_EXEMPLO['triangular']['funcao'],
            DISTRIBUICOES_EXEMPLO['triangular']['var'],
            DISTRIBUICOES_EXEMPLO['triangular']['dominio']
        )
        
        # Média da distribuição triangular simétrica no intervalo [0,1] é 0.5
        media = dist_tri.calcular_media()
        self.assertAlmostEqual(media, 0.5, places=6)

    def test_distribuicao_normal_aproximada(self):
        """Testa cálculos com a aproximação da distribuição normal."""
        dist_norm = DistribuicaoProbabilidade(
            DISTRIBUICOES_EXEMPLO['normal_aproximada']['funcao'],
            DISTRIBUICOES_EXEMPLO['normal_aproximada']['var'],
            DISTRIBUICOES_EXEMPLO['normal_aproximada']['dominio']
        )
        
        # Verifica se a probabilidade no intervalo [-1, 1] é aproximadamente 0.68
        prob = dist_norm.calcular_probabilidade((-1, 1))
        self.assertAlmostEqual(prob, 0.6827, places=2)

    def test_gerar_relatorio(self):
        """Testa a geração de relatório."""
        relatorio = self.dist_exp.gerar_relatorio()
        
        # Verifica se o relatório contém todas as informações necessárias
        self.assertIn('funcao', relatorio)
        self.assertIn('dominio', relatorio)
        self.assertIn('media', relatorio)
        self.assertIn('variancia', relatorio)
        self.assertIn('desvio_padrao', relatorio)
        self.assertIn('relatorio_latex', relatorio)

if __name__ == '__main__':
    unittest.main()