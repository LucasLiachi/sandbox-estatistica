"""
Implementação da Distribuição de Poisson para cálculos probabilísticos.

Este módulo fornece funções para calcular probabilidades usando a distribuição
de Poisson, incluindo probabilidades pontuais e acumuladas, com suporte para
ajuste de períodos e validação de parâmetros.
"""

import math
from typing import Tuple, Union
import logging
from dataclasses import dataclass
from typing import List, Dict

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@dataclass
class PoissonParams:
    """Parâmetros para cálculos da distribuição de Poisson."""
    lambda_val: float
    k: int
    periodo_dias: int = 30

@dataclass
class PoissonResult:
    """Resultados dos cálculos da distribuição de Poisson."""
    probabilidade: float
    lambda_ajustado: float
    percentual: str
    detalhes: Dict[str, float]

class CalculadoraPoisson:
    """Classe principal para cálculos da distribuição de Poisson."""
    
    def __init__(self, periodo_base: int = 30):
        self.periodo_base = periodo_base
    
    def validar_parametros(self, params: PoissonParams) -> None:
        """Validação dos parâmetros de entrada."""
        if not isinstance(params.k, int):
            raise TypeError("k deve ser um número inteiro")
        if params.k < 0:
            raise ValueError("k deve ser não-negativo")
        if params.lambda_val <= 0:
            raise ValueError("lambda deve ser positivo")
        if not isinstance(params.periodo_dias, int):
            raise TypeError("O período deve ser um número inteiro")
        if params.periodo_dias <= 0 or params.periodo_dias > 30:
            raise ValueError("O período deve estar entre 1 e 30 dias")

    def ajustar_lambda(self, lambda_val: float, periodo_dias: int) -> float:
        """Ajusta o parâmetro λ para o período especificado."""
        return lambda_val * (periodo_dias / self.periodo_base)

    def calcular_probabilidade_pontual(self, k: int, lambda_val: float) -> float:
        """Calcula P(X = k) para a distribuição de Poisson."""
        log_p = k * math.log(lambda_val) - lambda_val - math.log(math.factorial(k))
        return math.exp(log_p)

    def calcular_probabilidade_acumulada(self, k_max: int, lambda_val: float) -> float:
        """Calcula P(X ≤ k) para a distribuição de Poisson."""
        return sum(self.calcular_probabilidade_pontual(i, lambda_val) 
                  for i in range(k_max + 1))

    def calcular_probabilidade_complementar(self, k_max: int, lambda_val: float) -> float:
        """Calcula P(X > k) para a distribuição de Poisson."""
        prob_acumulada = self.calcular_probabilidade_acumulada(k_max, lambda_val)
        return round(1 - prob_acumulada, 4)
    
    def converter_para_percentual(self, valor: float) -> str:
        """Converte uma probabilidade para formato percentual."""
        return f"{valor * 100:.2f}%"

    def calcular(self, params: PoissonParams) -> PoissonResult:
        """Executa o cálculo completo da probabilidade de Poisson."""
        self.validar_parametros(params)
        
        # Ajuste do lambda para o período
        lambda_ajustado = self.ajustar_lambda(params.lambda_val, params.periodo_dias)
        logging.info(f"Lambda ajustado para {params.periodo_dias} dias: {lambda_ajustado}")
        
        # Cálculo da probabilidade
        prob = self.calcular_probabilidade_pontual(params.k, lambda_ajustado)
        logging.info(f"Probabilidade calculada: {prob}")
        
        # Detalhes do cálculo
        detalhes = {
            'lambda_original': params.lambda_val,
            'lambda_ajustado': lambda_ajustado,
            'k': params.k,
            'periodo_dias': params.periodo_dias,
            'log_probabilidade': math.log(prob) if prob > 0 else float('-inf')
        }
        
        return PoissonResult(
            probabilidade=prob,
            lambda_ajustado=lambda_ajustado,
            percentual=f"{prob * 100:.2f}%",
            detalhes=detalhes
        )

class ExemplosPoisson:
    """Exemplos práticos de uso da distribuição de Poisson."""
    
    def __init__(self):
        self.calculadora = CalculadoraPoisson()

    def exemplo_rodoviaria(self, lambda_hora: float = 3, k_max: int = 5):
        """Demonstração: fluxo de passageiros em rodoviária."""
        print("\nExemplo: Fluxo de Passageiros em Rodoviária")
        params = PoissonParams(lambda_val=lambda_hora, k=k_max, periodo_dias=1)
        
        prob_acumulada = self.calculadora.calcular_probabilidade_acumulada(
            k_max, params.lambda_val
        )
        print(f"P(X ≤ {k_max}) = {prob_acumulada:.4f}")

    def exemplo_falhas(self, intervalo_falhas: Tuple[float, float], 
                      periodo_dias: int, k: int = 2):
        """Demonstração: análise de falhas em equipamentos."""
        print("\nExemplo: Falhas em Equipamentos")
        
        a, b = intervalo_falhas
        lambda_base = (a + b) / 2
        
        params = PoissonParams(
            lambda_val=lambda_base,
            k=k,
            periodo_dias=periodo_dias
        )
        
        resultado = self.calculadora.calcular(params)
        print(f"Probabilidade: {resultado.probabilidade:.6f}")
        print(f"Percentual: {resultado.percentual}")

    def exemplo_caso_detalhado(self, lambda_val: float = 3, k_max: int = 2):
        """Demonstração detalhada do cálculo de probabilidades."""
        print(f"\nCaso Detalhado: P(X≤{k_max}) com λ={lambda_val}")
        
        # Calculando cada termo individualmente
        probabilidades = [
            self.calculadora.calcular_probabilidade_pontual(k, lambda_val)
            for k in range(k_max + 1)
        ]
        
        # Exibindo resultados parciais
        for k, p in enumerate(probabilidades):
            print(f"P(X={k}) = {p:.6f}")
        
        # Soma para probabilidade acumulada
        prob_acumulada = sum(probabilidades)
        print(f"P(X≤{k_max}) = {prob_acumulada:.6f}")

    def exemplo_caixa_eletronico(self, lambda_val: float = 1.6, k_max: int = 2):
        """
        Demonstração: Análise de fluxo em caixas eletrônicos.
        Calcula a probabilidade de ter mais que k_max clientes em espera.
        """
        print("\nExemplo: Fluxo em Caixa Eletrônico")
        print(f"Taxa média (λ) = {lambda_val} clientes/minuto")
        print(f"Analisando P(X > {k_max}) clientes em espera")
        
        params = PoissonParams(
            lambda_val=lambda_val,
            k=k_max,
            periodo_dias=1
        )
        
        prob_complementar = self.calculadora.calcular_probabilidade_complementar(
            k_max, lambda_val
        )
        percentual = self.calculadora.converter_para_percentual(prob_complementar)
        
        print(f"Probabilidade: {prob_complementar:.4f}")
        print(f"Percentual: {percentual}")
        print("Interpretação: Probabilidade de haver mais que " 
              f"{k_max} clientes em espera é {percentual}")

def main():
    """Função principal para demonstração dos cálculos."""
    exemplos = ExemplosPoisson()
    
    # Executar exemplos práticos
    exemplos.exemplo_rodoviaria()
    exemplos.exemplo_falhas((2, 4), 15)
    exemplos.exemplo_caso_detalhado()
    exemplos.exemplo_caixa_eletronico()  # Novo exemplo adicionado

if __name__ == "__main__":
    main()