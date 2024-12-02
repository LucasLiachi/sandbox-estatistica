
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

class PedidosSimulacao:
    def __init__(self, media_pedidos: float = 2, dias: int = 7, seed: int = 42):
        self.media_pedidos = media_pedidos
        self.dias = dias
        np.random.seed(seed)
        self.pedidos = self._gerar_pedidos()

    def _gerar_pedidos(self) -> np.ndarray:
        """Gera pedidos usando distribuição Poisson"""
        return np.random.poisson(lam=self.media_pedidos, size=self.dias)

    def plotar_histograma(self) -> None:
        """Plota o histograma dos pedidos"""
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
        """Calcula expectativa e probabilidades"""
        expectativa = np.mean(self.pedidos)
        probabilidades = self.pedidos / len(self.pedidos)
        return expectativa, probabilidades

    def exibir_resultados(self) -> None:
        """Exibe todos os resultados da simulação"""
        expectativa, probabilidades = self.calcular_estatisticas()
        
        print(f'Expectativa de pedidos por dia: {expectativa:.2f}')
        print('Probabilidade de pedidos por dia:')
        for dia, prob in enumerate(probabilidades, start=1):
            print(f'Dia {dia}: {prob:.2f}')
        print(f'Número total de dias analisados: {self.dias}')

def main():
    simulacao = PedidosSimulacao()
    simulacao.plotar_histograma()
    simulacao.exibir_resultados()

if __name__ == '__main__':
    main()