"""
Testes unitários para o módulo de distribuição binomial.
"""

import unittest
import numpy as np
from conceitos.basicos.binomial import DistribuicaoBinomial, calcular_probabilidade_binomial

class TestDistribuicaoBinomial(unittest.TestCase):
    def setUp(self):
        """Define dados de teste para uso nos casos de teste."""
        self.n = 10
        self.p = 0.5
        self.dist = DistribuicaoBinomial(self.n, self.p)

    def test_validar_parametros_validos(self):
        """Testa a validação com parâmetros válidos."""
        try:
            DistribuicaoBinomial(5, 0.3)
        except (ValueError, TypeError):
            self.fail("DistribuicaoBinomial() levantou erro inesperadamente!")

    def test_validar_n_negativo(self):
        """Testa a validação com n negativo."""
        with self.assertRaises(ValueError):
            DistribuicaoBinomial(-1, 0.5)

    def test_validar_p_invalido(self):
        """Testa a validação com p fora do intervalo [0,1]."""
        with self.assertRaises(ValueError):
            DistribuicaoBinomial(5, 1.5)
        with self.assertRaises(ValueError):
            DistribuicaoBinomial(5, -0.1)

    def test_validar_n_nao_inteiro(self):
        """Testa a validação com n não inteiro."""
        with self.assertRaises(TypeError):
            DistribuicaoBinomial(5.5, 0.5)

    def test_coeficiente_binomial(self):
        """Testa o cálculo do coeficiente binomial."""
        self.assertEqual(self.dist.calcular_coeficiente_binomial(0), 1)
        self.assertEqual(self.dist.calcular_coeficiente_binomial(1), 10)
        self.assertEqual(self.dist.calcular_coeficiente_binomial(2), 45)

    def test_pmf(self):
        """Testa o cálculo da função massa de probabilidade."""
        # Para n=10, p=0.5, k=5, a probabilidade é aproximadamente 0.246
        prob = self.dist.pmf(5)
        self.assertAlmostEqual(prob, 0.246, places=3)

    def test_cdf(self):
        """Testa o cálculo da função de distribuição acumulada."""
        # Para n=10, p=0.5, a probabilidade acumulada até k=5 deve ser > 0.5
        prob_acum = self.dist.cdf(5)
        self.assertGreater(prob_acum, 0.5)
        self.assertLess(prob_acum, 1.0)

    def test_sf(self):
        """Testa o cálculo da função de sobrevivência."""
        # A função de sobrevivência deve ser complementar à CDF
        k = 5
        self.assertAlmostEqual(self.dist.sf(k) + self.dist.cdf(k), 1.0)

    def test_wrapper_function(self):
        """Testa a função wrapper calcular_probabilidade_binomial."""
        prob_wrapper = calcular_probabilidade_binomial(self.n, 5, self.p)
        prob_class = self.dist.pmf(5)
        self.assertAlmostEqual(prob_wrapper, prob_class)

    def test_probabilidades_somam_um(self):
        """Testa se as probabilidades de todos os eventos possíveis somam 1."""
        total_prob = sum(self.dist.pmf(k) for k in range(self.n + 1))
        self.assertAlmostEqual(total_prob, 1.0)

    def test_casos_extremos(self):
        """Testa casos extremos da distribuição."""
        # Probabilidade 1 de sucesso
        dist_certa = DistribuicaoBinomial(5, 1.0)
        self.assertAlmostEqual(dist_certa.pmf(5), 1.0)
        self.assertAlmostEqual(dist_certa.pmf(4), 0.0)

        # Probabilidade 0 de sucesso
        dist_impossivel = DistribuicaoBinomial(5, 0.0)
        self.assertAlmostEqual(dist_impossivel.pmf(0), 1.0)
        self.assertAlmostEqual(dist_impossivel.pmf(1), 0.0)

if __name__ == '__main__':
    unittest.main()