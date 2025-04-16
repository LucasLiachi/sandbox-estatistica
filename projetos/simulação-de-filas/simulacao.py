#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from abc import ABC, abstractmethod
from typing import Dict, Any
import argparse
import json
from dataclasses import dataclass
from pathlib import Path

# Parâmetros configuráveis da simulação
SIMULATION_PARAMS = {
    # Parâmetros de chegada de pacientes (1 paciente a cada 30 minutos = 2 por hora)
    'DEFAULT_ARRIVAL_RATE': 2.0,     # Taxa média de chegada de pacientes por hora
    
    # Parâmetros de atendimento (1 paciente a cada 20 minutos = 3 por hora)
    'DEFAULT_SERVICE_RATE': 3.0,     # Taxa média de atendimento por médico por hora
    
    # Parâmetros de tempo
    'DEFAULT_SIMULATION_TIME': 8.0,   # Tempo padrão de simulação em horas
    
    # Parâmetros estatísticos
    'CONFIDENCE_LEVEL': 0.95,        # Nível de confiança para intervalos
    'TARGET_WAIT_TIME': 0.5,         # Tempo de espera alvo em horas
}

@dataclass
class SimulationConfig:
    """Configuração para simulação de filas."""
    arrival_rate: float  # Taxa de chegada (λ) - pacientes por hora
    service_rate: float  # Taxa de serviço (μ) - pacientes por hora por médico
    simulation_time: float = 8.0  # Tempo de simulação em horas
    time_unit: str = "hours"  # Unidade de tempo (hours, minutes)
    confidence_level: float = 0.95  # Nível de confiança para intervalos
    
    @classmethod
    def from_json(cls, json_path: str) -> 'SimulationConfig':
        """Carrega configuração de um arquivo JSON."""
        with open(json_path, 'r') as f:
            config = json.load(f)
        return cls(**config)
    
    def to_json(self, json_path: str) -> None:
        """Salva configuração em um arquivo JSON."""
        with open(json_path, 'w') as f:
            json.dump(self.__dict__, f, indent=4)
    
    def convert_to_hourly_rates(self) -> None:
        """Converte taxas para base horária se necessário."""
        if self.time_unit == "minutes":
            self.arrival_rate = self.arrival_rate * 60
            self.service_rate = self.service_rate * 60
            self.simulation_time = self.simulation_time / 60
            self.time_unit = "hours"

class QueueingModel(ABC):
    """Classe base para modelos de teoria das filas."""
    
    def __init__(self, config: SimulationConfig):
        """
        Inicializa o modelo com configurações.
        
        Args:
            config: Configuração da simulação
        """
        self.config = config
        self.config.convert_to_hourly_rates()
        self._validate_parameters()
    
    def _validate_parameters(self):
        """Valida parâmetros básicos do sistema."""
        if self.config.arrival_rate <= 0 or self.config.service_rate <= 0:
            raise ValueError("Taxas de chegada e serviço devem ser positivas")
    
    @property
    @abstractmethod
    def utilization(self) -> float:
        """Calcula utilização do sistema (ρ)."""
        pass
    
    @property
    @abstractmethod
    def average_queue_length(self) -> float:
        """Calcula número médio de clientes na fila (Lq)."""
        pass
    
    @property
    @abstractmethod
    def average_queue_time(self) -> float:
        """Calcula tempo médio na fila (Wq)."""
        pass
    
    def get_metrics(self) -> Dict[str, float]:
        """Retorna todas as métricas do modelo."""
        return {
            "utilization": self.utilization,
            "average_queue_length": self.average_queue_length,
            "average_queue_time": self.average_queue_time,
        }

class MM1Model(QueueingModel):
    """Implementação do modelo M/M/1."""
    
    def _validate_parameters(self):
        """Valida parâmetros específicos do M/M/1."""
        super()._validate_parameters()
        if self.config.arrival_rate >= self.config.service_rate:
            raise ValueError("Sistema instável: taxa de chegada deve ser menor que taxa de serviço")
    
    @property
    def utilization(self) -> float:
        """Calcula utilização do sistema (ρ = λ/μ)."""
        return self.config.arrival_rate / self.config.service_rate
    
    @property
    def average_queue_length(self) -> float:
        """Calcula número médio de clientes na fila."""
        rho = self.utilization
        return (rho * rho) / (1 - rho)
    
    @property
    def average_queue_time(self) -> float:
        """Calcula tempo médio na fila."""
        return self.average_queue_length / self.config.arrival_rate

class MM2Model(QueueingModel):
    """Implementação do modelo M/M/2."""
    
    def _validate_parameters(self):
        """Valida parâmetros específicos do M/M/2."""
        super()._validate_parameters()
        if self.config.arrival_rate >= 2 * self.config.service_rate:
            raise ValueError("Sistema instável: taxa de chegada deve ser menor que taxa total de serviço")
    
    @property
    def utilization(self) -> float:
        """Calcula utilização do sistema (ρ = λ/2μ)."""
        return self.config.arrival_rate / (2 * self.config.service_rate)
    
    def _p0(self) -> float:
        """Calcula P0 (probabilidade de sistema vazio)."""
        rho = self.config.arrival_rate / self.config.service_rate
        return 1 / (1 + rho + (rho * rho) / 2)
    
    @property
    def average_queue_length(self) -> float:
        """Calcula número médio de clientes na fila."""
        rho = self.config.arrival_rate / self.config.service_rate
        p0 = self._p0()
        return (rho * rho * p0) / (2 * (1 - rho/2))
    
    @property
    def average_queue_time(self) -> float:
        """Calcula tempo médio na fila."""
        return self.average_queue_length / self.config.arrival_rate

class HospitalQueueAnalyzer:
    """Classe para análise e comparação de diferentes cenários de filas hospitalares."""
    
    def __init__(self, config: SimulationConfig):
        """
        Inicializa analisador com configurações.
        
        Args:
            config: Configuração da simulação
        """
        self.config = config
        self.mm1 = MM1Model(config)
        self.mm2 = MM2Model(config)
    
    def compare_models(self) -> pd.DataFrame:
        """Compara métricas entre modelos M/M/1 e M/M/2."""
        metrics = {
            'Metric': ['Utilization', 'Avg Queue Length', f'Avg Wait Time ({self.config.time_unit})'],
            'Single Doctor': [
                self.mm1.utilization,
                self.mm1.average_queue_length,
                self.mm1.average_queue_time
            ],
            'Two Doctors': [
                self.mm2.utilization,
                self.mm2.average_queue_length,
                self.mm2.average_queue_time
            ]
        }
        return pd.DataFrame(metrics)
    
    def plot_comparison(self, save_path: str = None):
        """Cria visualização comparando modelos M/M/1 e M/M/2."""
        metrics = self.compare_models()
        
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        fig.suptitle('Hospital Queue Performance Comparison')
        
        for idx, metric in enumerate(metrics['Metric']):
            axes[idx].bar(['Single Doctor', 'Two Doctors'],
                         [metrics['Single Doctor'][idx], metrics['Two Doctors'][idx]])
            axes[idx].set_title(metric)
            axes[idx].set_ylabel('Value')
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()
    
    def save_results(self, output_dir: str):
        """Salva resultados da análise em arquivos."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Salva configuração
        self.config.to_json(str(output_path / "config.json"))
        
        # Salva métricas em CSV
        self.compare_models().to_csv(str(output_path / "metrics.csv"), index=False)
        
        # Salva gráficos
        self.plot_comparison(str(output_path / "comparison.png"))

def main():
    """Interface de linha de comando para análise de filas hospitalares."""
    parser = argparse.ArgumentParser(description='Hospital Queue Analysis')
    parser.add_argument('--config', type=str, help='Caminho para arquivo de configuração JSON')
    parser.add_argument('--arrival-rate', type=float, help='Taxa média de chegada de pacientes')
    parser.add_argument('--service-rate', type=float, help='Taxa média de atendimento por médico')
    parser.add_argument('--time-unit', choices=['minutes', 'hours'], default='hours',
                       help='Unidade de tempo para as taxas')
    parser.add_argument('--output-dir', type=str, help='Diretório para salvar resultados')
    
    args = parser.parse_args()
    
    try:
        if args.config:
            config = SimulationConfig.from_json(args.config)
        else:
            if not args.arrival_rate or not args.service_rate:
                raise ValueError("Deve fornecer arquivo de configuração ou taxas de chegada e serviço")
            config = SimulationConfig(
                arrival_rate=args.arrival_rate,
                service_rate=args.service_rate,
                time_unit=args.time_unit
            )
        
        analyzer = HospitalQueueAnalyzer(config)
        
        print("\nQueue Analysis Results:")
        print("=" * 50)
        print(analyzer.compare_models().to_string(index=False))
        
        print("\nGenerating visualization...")
        if args.output_dir:
            analyzer.save_results(args.output_dir)
        else:
            analyzer.plot_comparison()
        
        improvement = ((analyzer.mm1.average_queue_time - analyzer.mm2.average_queue_time) 
                      / analyzer.mm1.average_queue_time * 100)
        print(f"\nAdding a second doctor reduces average wait time by {improvement:.1f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()