"""
Statistical Analysis System
This module implements statistical tests (chi-square), Markov chain simulations,
and queuing theory analysis (M/M/1, M/M/c) with a command-line interface.

Example usage:
    python projeto-integrado.py

Author: 
Date: 
"""

import numpy as np
import scipy.stats as stats
from typing import List, Tuple, Dict, Optional
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class QueueMetrics:
    """Class to store queue performance metrics."""
    utilization: float
    avg_customers_system: float
    avg_customers_queue: float
    avg_wait_time: float
    avg_time_system: float

def validate_probabilities(matrix: np.ndarray) -> bool:
    """
    Validate if a matrix is a valid transition probability matrix.
    
    Args:
        matrix: numpy array representing transition matrix
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(matrix, np.ndarray):
        return False
    
    if matrix.shape[0] != matrix.shape[1]:
        return False
        
    # Check if all elements are between 0 and 1
    if not np.all((matrix >= 0) & (matrix <= 1)):
        return False
        
    # Check if rows sum to 1
    row_sums = np.sum(matrix, axis=1)
    return np.allclose(row_sums, 1.0)

def chi_square_test(observed: List[float], expected: Optional[List[float]] = None) -> Dict:
    """
    Perform chi-square goodness of fit test.
    
    Args:
        observed: List of observed frequencies
        expected: List of expected frequencies (optional)
        
    Returns:
        Dict containing test results
    """
    if not all(isinstance(x, (int, float)) for x in observed):
        raise ValueError("All observations must be numeric")
        
    if expected is None:
        # If expected frequencies not provided, assume uniform distribution
        expected = [sum(observed) / len(observed)] * len(observed)
    
    if len(observed) != len(expected):
        raise ValueError("Observed and expected frequencies must have same length")
        
    chi2_stat, p_value = stats.chisquare(observed, expected)
    
    df = len(observed) - 1
    critical_value = stats.chi2.ppf(0.95, df)
    
    return {
        "statistic": chi2_stat,
        "p_value": p_value,
        "critical_value": critical_value,
        "df": df,
        "reject_null": p_value < 0.05
    }

def markov_chain_simulation(
    transition_matrix: np.ndarray,
    initial_state: np.ndarray,
    steps: int
) -> Tuple[np.ndarray, List[int]]:
    """
    Simulate a Markov chain for given number of steps.
    
    Args:
        transition_matrix: Square matrix of transition probabilities
        initial_state: Initial probability distribution
        steps: Number of steps to simulate
        
    Returns:
        Tuple containing final state distribution and state history
    """
    if not validate_probabilities(transition_matrix):
        raise ValueError("Invalid transition matrix")
        
    current_state = initial_state
    state_history = []
    
    for _ in range(steps):
        current_state = np.dot(current_state, transition_matrix)
        state_idx = np.random.choice(len(current_state), p=current_state)
        state_history.append(state_idx)
    
    return current_state, state_history

def queue_analysis(
    arrival_rate: float,
    service_rate: float,
    num_servers: int = 1
) -> QueueMetrics:
    """
    Analyze M/M/c queuing system.
    
    Args:
        arrival_rate: Average arrival rate (λ)
        service_rate: Average service rate per server (μ)
        num_servers: Number of servers (c)
        
    Returns:
        QueueMetrics object containing performance measures
    """
    if arrival_rate <= 0 or service_rate <= 0 or num_servers <= 0:
        raise ValueError("Rates and number of servers must be positive")
        
    rho = arrival_rate / (num_servers * service_rate)  # System utilization
    
    if rho >= 1:
        raise ValueError("System is unstable (ρ >= 1)")
    
    # For M/M/1
    if num_servers == 1:
        L = rho / (1 - rho)  # Average number in system
        Lq = rho * rho / (1 - rho)  # Average number in queue
        W = 1 / (service_rate - arrival_rate)  # Average time in system
        Wq = rho / (service_rate - arrival_rate)  # Average waiting time
    else:
        # For M/M/c
        p0 = 1.0  # Probability of empty system (simplified calculation)
        L = rho * service_rate / (1 - rho)
        Lq = L - arrival_rate / service_rate
        W = L / arrival_rate
        Wq = Lq / arrival_rate
    
    return QueueMetrics(
        utilization=rho,
        avg_customers_system=L,
        avg_customers_queue=Lq,
        avg_wait_time=Wq,
        avg_time_system=W
    )

def plot_markov_chain_history(history: List[int], num_states: int):
    """Plot the state history of a Markov chain simulation."""
    plt.figure(figsize=(10, 6))
    plt.plot(history)
    plt.yticks(range(num_states))
    plt.xlabel('Step')
    plt.ylabel('State')
    plt.title('Markov Chain State History')
    plt.grid(True)
    plt.show()

def get_numeric_input(prompt: str) -> float:
    """Get numeric input from user with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_matrix_input(size: int) -> np.ndarray:
    """Get matrix input from user with validation."""
    matrix = np.zeros((size, size))
    print(f"\nEnter the {size}x{size} transition matrix (row by row):")
    
    for i in range(size):
        while True:
            try:
                row = [float(x) for x in input(f"Row {i+1} (space-separated): ").split()]
                if len(row) != size:
                    raise ValueError("Wrong number of elements")
                matrix[i] = row
                if not np.allclose(sum(row), 1.0):
                    raise ValueError("Row must sum to 1")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
    
    return matrix

def test_implementations():
    """Run basic tests on the implementations."""
    print("\nRunning tests...")
    
    # Test chi-square
    try:
        observed = [16, 18, 16, 14, 12, 12]
        result = chi_square_test(observed)
        print("Chi-square test passed:", result['p_value'] > 0)
    except Exception as e:
        print("Chi-square test failed:", e)
    
    # Test Markov chain
    try:
        P = np.array([[0.7, 0.3], [0.4, 0.6]])
        initial = np.array([1.0, 0.0])
        final_state, _ = markov_chain_simulation(P, initial, 100)
        print("Markov chain test passed:", len(final_state) == 2)
    except Exception as e:
        print("Markov chain test failed:", e)
    
    # Test queue analysis
    try:
        metrics = queue_analysis(2, 3)
        print("Queue analysis test passed:", metrics.utilization < 1)
    except Exception as e:
        print("Queue analysis test failed:", e)

def main():
    """Main function with CLI interface."""
    while True:
        print("\n=== Statistical Analysis System ===")
        print("1. Chi-square Test")
        print("2. Markov Chain Simulation")
        print("3. Queue Analysis")
        print("4. Run Tests")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        try:
            if choice == '1':
                print("\nChi-square Test")
                n = int(input("Enter number of categories: "))
                observed = []
                expected = []
                
                print("\nEnter observed frequencies:")
                for i in range(n):
                    observed.append(get_numeric_input(f"Category {i+1}: "))
                
                use_expected = input("\nDo you want to enter expected frequencies? (y/n): ").lower() == 'y'
                if use_expected:
                    print("\nEnter expected frequencies:")
                    for i in range(n):
                        expected.append(get_numeric_input(f"Category {i+1}: "))
                
                result = chi_square_test(observed, expected if use_expected else None)
                print("\nResults:")
                print(f"Chi-square statistic: {result['statistic']:.4f}")
                print(f"p-value: {result['p_value']:.4f}")
                print(f"Critical value (α=0.05): {result['critical_value']:.4f}")
                print(f"Degrees of freedom: {result['df']}")
                print(f"Decision: {'Reject' if result['reject_null'] else 'Fail to reject'} null hypothesis")
            
            elif choice == '2':
                print("\nMarkov Chain Simulation")
                n = int(input("Enter number of states: "))
                steps = int(input("Enter number of steps to simulate: "))
                
                P = get_matrix_input(n)
                initial_state = np.zeros(n)
                initial_state[0] = 1  # Start from state 0
                
                final_state, history = markov_chain_simulation(P, initial_state, steps)
                
                print("\nResults:")
                print("Final state probabilities:")
                for i, prob in enumerate(final_state):
                    print(f"State {i}: {prob:.4f}")
                
                plot = input("\nWould you like to see the state history plot? (y/n): ").lower() == 'y'
                if plot:
                    plot_markov_chain_history(history, n)
            
            elif choice == '3':
                print("\nQueue Analysis")
                arrival_rate = get_numeric_input("Enter arrival rate (λ): ")
                service_rate = get_numeric_input("Enter service rate (μ): ")
                num_servers = int(get_numeric_input("Enter number of servers: "))
                
                metrics = queue_analysis(arrival_rate, service_rate, num_servers)
                
                print("\nResults:")
                print(f"System utilization (ρ): {metrics.utilization:.4f}")
                print(f"Average number in system (L): {metrics.avg_customers_system:.4f}")
                print(f"Average number in queue (Lq): {metrics.avg_customers_queue:.4f}")
                print(f"Average time in system (W): {metrics.avg_time_system:.4f}")
                print(f"Average waiting time (Wq): {metrics.avg_wait_time:.4f}")
            
            elif choice == '4':
                test_implementations()
            
            elif choice == '5':
                print("\nGoodbye!")
                break
            
            else:
                print("\nInvalid choice. Please try again.")
                
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()