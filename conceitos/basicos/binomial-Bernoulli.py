from scipy.stats import binom
import matplotlib.pyplot as plt

def analyze_binomial_distribution(n=5, p=0.8):
    """
    Analyze and plot binomial distribution for given n and p
    """
    # Generate possible values
    r_values = list(range(n + 1))
    
    # Calculate statistics
    mean, var = binom.stats(n, p)
    probabilities = [binom.pmf(r, n, p) for r in r_values]
    
    # Print probability table
    print("r\tp(r)")
    for r, prob in zip(r_values, probabilities):
        print(f"{r}\t{prob:.4f}")
    print(f"mean = {mean}")
    print(f"variance = {var}")
    
    # Plot distribution
    plt.bar(r_values, probabilities)
    plt.title(f"Binomial Distribution (n={n}, p={p})")
    plt.xlabel("Number of successes (r)")
    plt.ylabel("Probability")
    plt.show()

# Example usage
analyze_binomial_distribution(5, 0.8)

