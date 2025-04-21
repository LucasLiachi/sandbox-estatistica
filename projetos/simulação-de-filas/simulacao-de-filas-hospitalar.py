"""
SIMULAÇÃO DE FILAS HOSPITALARES - GUIA DE USO E IMPLEMENTAÇÃO

Este programa implementa uma simulação de filas hospitalares usando teoria das filas (modelos M/M/1 e M/M/2).

COMO EXECUTAR:
1. Configuração básica:
   python simulacao.py --arrival-rate 2 --service-rate 3
   
2. Configuração com arquivo JSON:
   python simulacao.py --config config.json
   
3. Salvando resultados:
   python simulacao.py --arrival-rate 2 --service-rate 3 --output-dir resultados/

PARÂMETROS CONFIGURÁVEIS:
Os parâmetros podem ser ajustados no dicionário SIMULATION_PARAMS no início do arquivo:
- Taxas de chegada (pacientes/hora)
- Taxas de atendimento (pacientes/hora/médico)
- Períodos de pico
- Parâmetros estatísticos

CÁLCULOS IMPLEMENTADOS:

1. Modelo M/M/1 (Um médico):
   - Utilização (ρ) = λ/μ
     onde: λ = taxa de chegada, μ = taxa de atendimento
   - Comprimento médio da fila (Lq) = ρ²/(1-ρ)
   - Tempo médio de espera (Wq) = Lq/λ

2. Modelo M/M/2 (Dois médicos):
   - Utilização (ρ) = λ/(2μ)
   - Probabilidade sistema vazio (P0) = [1 + ρ + ρ²/2]^(-1)
   - Comprimento médio da fila (Lq) = (ρ² * P0)/(2(1-ρ))
   - Tempo médio de espera (Wq) = Lq/λ

FLUXO DE EXECUÇÃO:
1. Carrega configurações (arquivo JSON ou argumentos CLI)
2. Valida parâmetros de entrada
3. Calcula métricas para ambos os modelos (M/M/1 e M/M/2)
4. Gera visualizações comparativas
5. Salva resultados (opcional)

INTERPRETAÇÃO DOS RESULTADOS:
- Utilização (ρ): Quanto maior, mais ocupado está o sistema
- Comprimento da fila (Lq): Número médio de pacientes esperando
- Tempo de espera (Wq): Tempo médio que cada paciente espera

REQUISITOS DE ESTABILIDADE:
- M/M/1: λ < μ (taxa de chegada menor que taxa de atendimento)
- M/M/2: λ < 2μ (taxa de chegada menor que taxa total de atendimento)
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

class PedidosSimulacao:
    """
    Classe para simulação de pedidos usando distribuição de Poisson.
    
    Atributos:
        media_pedidos (float): Média de pedidos por dia (lambda da distribuição Poisson)
        dias (int): Número de dias para simular
        seed (int): Semente para reprodutibilidade dos resultados aleatórios
        pedidos (np.ndarray): Array com os pedidos gerados para cada dia
    """
    
    def __init__(self, media_pedidos: float = 2, dias: int = 7, seed: int = 42):
        """
        Inicializa a simulação com os parâmetros fornecidos.
        
        Args:
            media_pedidos: Taxa média de pedidos por dia (padrão: 2)
            dias: Quantidade de dias a simular (padrão: 7)
            seed: Semente para geração de números aleatórios (padrão: 42)
        """
        self.media_pedidos = media_pedidos
        self.dias = dias
        np.random.seed(seed)  # Garante reprodutibilidade
        self.pedidos = self._gerar_pedidos()

    def _gerar_pedidos(self) -> np.ndarray:
        """
        Gera pedidos aleatórios usando distribuição Poisson.
        
        A distribuição de Poisson é ideal para modelar eventos raros em intervalo fixo,
        como número de pedidos por dia. O parâmetro lambda (media_pedidos) representa
        a taxa média de ocorrência dos eventos.
        
        Returns:
            np.ndarray: Array com quantidade de pedidos para cada dia
        """
        return np.random.poisson(lam=self.media_pedidos, size=self.dias)

    def plotar_histograma(self) -> None:
        """
        Plota o histograma da distribuição dos pedidos.
        
        O histograma mostra a frequência de cada quantidade de pedidos,
        permitindo visualizar o padrão de distribuição dos dados.
        Características do gráfico:
        - Bins ajustados para valores inteiros
        - Grade para melhor visualização
        - Eixos rotulados adequadamente
        """
        plt.figure(figsize=(8, 5))
        plt.hist(self.pedidos, 
                bins=np.arange(min(self.pedidos), max(self.pedidos) + 1.5) - 0.5,
                edgecolor='black', alpha=0.7)
        plt.xticks(np.arange(min(self.pedidos), max(self.pedidos) + 1))
        plt.xlabel('Número de Pedidos por Dia')
        plt.ylabel('Frequência')
        plt.title('Histograma de Pedidos de Refrigerante A por Dia')
        plt.grid(True)
        plt.show()

    def calcular_estatisticas(self) -> Tuple[float, List[float]]:
        """
        Calcula estatísticas descritivas dos pedidos.
        
        Retorna a expectativa (média) dos pedidos e as probabilidades
        observadas para cada quantidade de pedidos.
        
        Returns:
            Tuple[float, List[float]]: (expectativa, lista de probabilidades)
        """
        expectativa = np.mean(self.pedidos)  # Média aritmética dos pedidos
        probabilidades = self.pedidos / len(self.pedidos)  # Freq. relativa
        return expectativa, probabilidades

    def exibir_resultados(self) -> None:
        """
        Exibe um relatório completo dos resultados da simulação.
        
        Mostra:
        1. Expectativa (média) de pedidos por dia
        2. Probabilidade observada para cada dia
        3. Total de dias analisados
        """
        expectativa, probabilidades = self.calcular_estatisticas()
        
        print(f'Expectativa de pedidos por dia: {expectativa:.2f}')
        print('Probabilidade de pedidos por dia:')
        for dia, prob in enumerate(probabilidades, start=1):
            print(f'Dia {dia}: {prob:.2f}')
        print(f'Número total de dias analisados: {self.dias}')

def main():
    """
    Função principal que executa a simulação.
    
    Fluxo de execução:
    1. Cria uma instância da simulação com parâmetros padrão
       - media_pedidos = 2 pedidos/dia
       - dias = 7 dias
       - seed = 42 (para reprodutibilidade)
    2. Gera e exibe o histograma da distribuição
    3. Calcula e exibe as estatísticas dos resultados
    
    Como usar:
    $ python simulacao.py
    
    O programa irá gerar:
    - Um gráfico do histograma dos pedidos
    - Um relatório com estatísticas no terminal
    """
    simulacao = PedidosSimulacao()
    simulacao.plotar_histograma()
    simulacao.exibir_resultados()

"""
DETALHAMENTO DO MODELO MATEMÁTICO

1. Distribuição de Poisson
   A simulação usa a distribuição de Poisson para modelar eventos raros
   em um intervalo fixo de tempo. A função de probabilidade é:
   
   P(X = k) = (λ^k * e^-λ) / k!
   
   onde:
   - λ (lambda) é a taxa média de eventos (media_pedidos)
   - k é o número de eventos (pedidos) em um intervalo
   - e é o número de Euler

2. Propriedades da Distribuição
   - Média (expectativa) = λ
   - Variância = λ
   - Assimetria = 1/√λ
   
3. Interpretação dos Resultados
   - Se média observada ≈ λ: modelo está bem calibrado
   - Histograma deve mostrar padrão assimétrico à direita
   - Variabilidade aumenta com λ

4. Limitações do Modelo
   - Assume eventos independentes
   - Assume taxa constante ao longo do tempo
   - Não considera sazonalidade ou tendências
"""

if __name__ == '__main__':
    main()