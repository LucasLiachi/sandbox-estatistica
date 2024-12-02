# Success probability
p = 0.75
n = 5  # Number of trials
x = 5  # Number of successes

# Calculate P(X=x) using binomial probability
P_resultado = (p**x) * ((1-p)**(n-x))

print(P_resultado)
