import simpy
import numpy as np

class QueueSystem:
    def __init__(self, env, arrival_rate, service_shape, service_scale):
        self.env = env
        self.server = simpy.Resource(env, capacity=1)
        self.arrival_rate = arrival_rate
        self.service_shape = service_shape
        self.service_scale = service_scale
        self.waiting_times = []

    def arrival_process(self):
        customer_id = 1
        while True:
            inter_arrival_time = np.random.exponential(1/self.arrival_rate)
            yield self.env.timeout(inter_arrival_time)
            self.env.process(self.customer(customer_id))
            customer_id += 1

    def customer(self, customer_id):
        arrival_time = self.env.now
        with self.server.request() as req:
            yield req
            service_time = np.random.gamma(self.service_shape, self.service_scale)
            yield self.env.timeout(service_time)
            departure_time = self.env.now
            waiting_time = departure_time - arrival_time
            self.waiting_times.append(waiting_time)

def run_simulation(arrival_rate, service_shape, service_scale, sim_time):
    env = simpy.Environment()
    queue = QueueSystem(env, arrival_rate, service_shape, service_scale)
    env.process(queue.arrival_process())
    env.run(until=sim_time)
    
    avg_waiting_time = np.mean(queue.waiting_times)
    print(f"Average waiting time: {avg_waiting_time:.2f} time units")

# Exemplo de execução
if __name__ == '__main__':
    arrival_rate = 0.5  # taxa de chegada de clientes por unidade de tempo
    service_shape = 2   # parâmetro da forma da distribuição gamma
    service_scale = 1   # parâmetro de escala da distribuição gamma
    sim_time = 1000     # tempo de simulação
    
    run_simulation(arrival_rate, service_shape, service_scale, sim_time)
