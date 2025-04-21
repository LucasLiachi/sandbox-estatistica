"""
Módulo para análise e validação de funções densidade de probabilidade (PDF).

Este módulo implementa funcionalidades para:
- Validação de PDFs (positividade e integral unitária)
- Cálculo de probabilidades
- Visualização de distribuições
- Geração de relatórios em LaTeX

Author: Lucas
Date: 2025
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Union, Dict, Optional, List
from sympy.printing import latex
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PDFValidationError(Exception):
    """Custom exception for PDF validation errors"""
    pass

class DistribuicaoProbabilidade:
    """
    Implementa análise e visualização de funções densidade de probabilidade.
    
    Attributes:
        funcao (sp.Expr): Expressão simbólica da função
        var (sp.Symbol): Variável simbólica
        dominio (Tuple): Domínio da função (min, max)
    """
    
    def __init__(self, funcao_str: str, var: str, dominio: Tuple[Union[float, str], Union[float, str]]):
        """
        Inicializa a distribuição de probabilidade.

        Args:
            funcao_str: String representando a função
            var: Nome da variável
            dominio: Tupla (min, max) do domínio
        """
        self.var_name = var
        self.var = sp.Symbol(var, real=True)
        self.funcao = sp.sympify(funcao_str)
        self.dominio = dominio
        self._validar_distribuicao()
    
    def _validar_distribuicao(self) -> None:
        """Valida se a função é uma PDF válida."""
        self.verificar_positividade()
        self.verificar_integral_unitaria()
    
    def verificar_positividade(self) -> bool:
        """Verifica se a função é não-negativa em todo o domínio."""
        try:
            x = self.var
            funcao = self.funcao
            dominio = self.dominio
            
            # Verifica os pontos críticos (derivada = 0)
            derivada = sp.diff(funcao, x)
            pontos_criticos = sp.solve(derivada, x)
            
            # Adiciona extremos do domínio aos pontos de verificação
            pontos_teste = pontos_criticos + [dominio[0], dominio[1]]
            
            # Testa a função em cada ponto
            for ponto in pontos_teste:
                # Convert numeric types to sympy numbers
                if isinstance(ponto, (int, float)):
                    ponto = sp.Number(ponto)
                
                # Verifica se o ponto está no domínio
                if (isinstance(ponto, sp.Number) or ponto.is_real) and dominio[0] <= ponto <= dominio[1]:
                    valor = funcao.subs(x, ponto)
                    # Convert numeric result to sympy number if needed
                    if isinstance(valor, (int, float)):
                        valor = sp.Number(valor)
                    if (isinstance(valor, sp.Number) or valor.is_real) and valor < 0:
                        raise PDFValidationError(f"Função é negativa em x = {ponto}")
            
            return True
            
        except Exception as e:
            raise PDFValidationError(f"Erro ao verificar positividade: {str(e)}")
    
    def verificar_integral_unitaria(self, tolerancia: float = 1e-10) -> bool:
        """Verifica se a integral da função no domínio é igual a 1."""
        try:
            x = self.var
            funcao = self.funcao
            dominio = self.dominio
            
            integral = sp.integrate(funcao, (x, dominio[0], dominio[1]))
            valor_numerico = float(integral.evalf())
            
            if abs(valor_numerico - 1) > tolerancia:
                msg = f"Integral da função = {valor_numerico}, deve ser 1"
                raise PDFValidationError(msg)
            
            return True
            
        except Exception as e:
            raise PDFValidationError(f"Erro ao calcular integral: {str(e)}")
    
    def calcular_probabilidade(self, limite: Tuple[Union[float, str], Union[float, str]]) -> float:
        """
        Calcula a probabilidade P(a ≤ X ≤ b).

        Args:
            limite: Tupla (a, b) dos limites de integração

        Returns:
            Probabilidade calculada
        """
        try:
            prob = sp.integrate(self.funcao, (self.var, limite[0], limite[1]))
            return float(prob.evalf())
        except Exception as e:
            raise PDFValidationError(f"Erro ao calcular probabilidade: {str(e)}")
    
    def calcular_media(self) -> float:
        """Calcula a média (valor esperado) da distribuição."""
        try:
            media = sp.integrate(self.var * self.funcao, (self.var, self.dominio[0], self.dominio[1]))
            return float(media.evalf())
        except Exception as e:
            raise PDFValidationError(f"Erro ao calcular média: {str(e)}")
    
    def calcular_variancia(self) -> float:
        """Calcula a variância da distribuição."""
        try:
            media = self.calcular_media()
            var_func = (self.var - media)**2 * self.funcao
            variancia = sp.integrate(var_func, (self.var, self.dominio[0], self.dominio[1]))
            return float(variancia.evalf())
        except Exception as e:
            raise PDFValidationError(f"Erro ao calcular variância: {str(e)}")
    
    def plotar_distribuicao(self, titulo: Optional[str] = None, 
                           pontos: int = 1000, 
                           areas: Optional[List[Tuple[float, float]]] = None) -> None:
        """
        Plota a distribuição de probabilidade.

        Args:
            titulo: Título opcional para o gráfico
            pontos: Número de pontos para o plot
            areas: Lista de tuplas (a,b) para destacar áreas sob a curva
        """
        try:
            # Converter limites para float quando possível
            x_min = float(self.dominio[0]) if self.dominio[0] != float('-inf') else -10
            x_max = float(self.dominio[1]) if self.dominio[1] != float('inf') else 10
            
            x = np.linspace(x_min, x_max, pontos)
            y = [float(self.funcao.subs(self.var, xi).evalf()) for xi in x]
            
            plt.figure(figsize=(10, 6))
            plt.plot(x, y, 'b-', label='PDF')
            
            # Plotar áreas sob a curva se especificadas
            if areas:
                for a, b in areas:
                    mask = (x >= a) & (x <= b)
                    plt.fill_between(x[mask], y[mask], alpha=0.3)
                    prob = self.calcular_probabilidade((a, b))
                    plt.text((a+b)/2, max(y)/2, f'P({a}≤X≤{b})={prob:.4f}')
            
            plt.title(titulo or f'Distribuição de Probabilidade: {self.funcao}')
            plt.xlabel(self.var_name)
            plt.ylabel(f'f({self.var_name})')
            plt.grid(True, alpha=0.3)
            plt.legend()
            plt.show()
            
        except Exception as e:
            raise PDFValidationError(f"Erro ao plotar distribuição: {str(e)}")
    
    def gerar_relatorio(self) -> Dict:
        """
        Gera um relatório completo sobre a distribuição.

        Returns:
            Dicionário com resultados das análises
        """
        try:
            resultados = {
                'funcao': latex(self.funcao),
                'dominio': f"[{latex(self.dominio[0])}, {latex(self.dominio[1])}]",
                'media': self.calcular_media(),
                'variancia': self.calcular_variancia(),
                'desvio_padrao': np.sqrt(self.calcular_variancia())
            }
            
            # Gerar relatório LaTeX
            relatorio_latex = self._gerar_relatorio_latex(resultados)
            resultados['relatorio_latex'] = relatorio_latex
            
            return resultados
            
        except Exception as e:
            raise PDFValidationError(f"Erro ao gerar relatório: {str(e)}")
    
    def _gerar_relatorio_latex(self, resultados: Dict) -> str:
        """Gera relatório em formato LaTeX."""
        x = self.var
        relatorio = [
            "\\begin{document}",
            "\\section{Relatório de Validação de PDF}",
            f"\\subsection{{Função Analisada}}",
            f"f({self.var_name}) = {latex(self.funcao)}",
            f"\\subsection{{Domínio}}",
            f"[{latex(self.dominio[0])}, {latex(self.dominio[1])}]",
        ]
        
        for chave, valor in resultados.items():
            relatorio.append(f"\\subsection{{{chave}}}")
            relatorio.append(f"{latex(valor)}")
        
        relatorio.append("\\end{document}")
        return "\n".join(relatorio)

# Exemplos predefinidos de distribuições comuns
DISTRIBUICOES_EXEMPLO = {
    'exponencial': {
        'funcao': '2 * exp(-2*x)',
        'var': 'x',
        'dominio': (0, float('inf')),
        'descricao': 'Distribuição Exponencial (λ=2)'
    },
    'triangular': {
        'funcao': 'Piecewise((2*x, (x >= 0) & (x <= 1/2)), (2*(1-x), (x > 1/2) & (x <= 1)), (0, True))',
        'var': 'x',
        'dominio': (0, 1),
        'descricao': 'Distribuição Triangular'
    },
    'normal_aproximada': {
        'funcao': '(1/(sqrt(2*pi))) * exp(-(x**2)/2)',
        'var': 'x',
        'dominio': (float('-inf'), float('inf')),
        'descricao': 'Aproximação da Distribuição Normal Padrão'
    }
}

if __name__ == "__main__":
    # Demonstração com diferentes distribuições
    try:
        for nome, params in DISTRIBUICOES_EXEMPLO.items():
            logger.info(f"\nAnalisando {params['descricao']}:")
            dist = DistribuicaoProbabilidade(
                params['funcao'], 
                params['var'], 
                params['dominio']
            )
            
            # Calcular e mostrar estatísticas
            relatorio = dist.gerar_relatorio()
            logger.info(f"Média: {relatorio['media']:.4f}")
            logger.info(f"Desvio Padrão: {relatorio['desvio_padrao']:.4f}")
            
            # Plotar distribuição com algumas áreas de interesse
            if nome == 'normal_aproximada':
                areas = [(-1, 1), (-2, 2)]  # 68% e 95% para normal
            else:
                areas = [(0, 1)]  # área genérica para outras distribuições
                
            dist.plotar_distribuicao(
                titulo=params['descricao'],
                areas=areas
            )
            
    except PDFValidationError as e:
        logger.error(f"Erro: {str(e)}")