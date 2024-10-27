import numpy as np
import matplotlib.pyplot as plt

# Definir parâmetros
lambda_rate = 1  # taxa de chegada (clientes por minuto) sendo 2 clientes chegando a cada 2 minutos
mu_rate = 1 / 5  # taxa de serviço (atendimentos por minuto) sendo um tempo de atendimento de 5 minutos
n_atendentes = 3 # uma fila com 3 atendentes
simulation_time = 99.48  # tempo total de simulação (minutos)

# Função para simular chegadas e serviços
def simulate_queue(lambda_rate, mu_rate, n_atendentes, simulation_time):
    arrival_times = np.cumsum(np.random.exponential(1/lambda_rate, int(lambda_rate * simulation_time)))
    service_times = np.random.exponential(1/mu_rate, len(arrival_times))

    departure_times = np.zeros_like(arrival_times)
    queue_times = np.zeros_like(arrival_times)
    service_start_times = np.zeros_like(arrival_times)

    for i in range(len(arrival_times)):
        if i < n_atendentes:
            service_start_times[i] = arrival_times[i]
        else:
            service_start_times[i] = max(arrival_times[i], departure_times[i - n_atendentes])

        departure_times[i] = service_start_times[i] + service_times[i]
        queue_times[i] = service_start_times[i] - arrival_times[i]

    return arrival_times, queue_times, service_times, departure_times

# Executar simulação
arrival_times, queue_times, service_times, departure_times = simulate_queue(lambda_rate, mu_rate, n_atendentes, simulation_time)

# Calcular métricas
average_queue_time = np.mean(queue_times)
average_service_time = np.mean(service_times)
server_utilization = np.sum(service_times) / (simulation_time * n_atendentes)
average_clients_in_queue = np.mean([np.sum((arrival_times <= t) & (departure_times > t)) for t in arrival_times])

# Exibir resultados
print(f"Tempo médio na fila: {average_queue_time:.2f} minutos")
print(f"Tempo médio de atendimento: {average_service_time:.2f} minutos")
print(f"Utilização do servidor: {server_utilization:.2%}")
print(f"Número médio de clientes na fila: {average_clients_in_queue:.2f}")

# Plotar histograma das ocorrências de chegada
plt.hist(np.diff(np.insert(arrival_times, 0, 0)), bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Intervalo de Tempo Entre Chegadas (minutos)')
plt.ylabel('Frequência')
plt.title('Histograma dos Tempos Entre Chegadas')
plt.show()
