#probabilidade de sucesso 
p = 0.75
#Número de repetições de testes
n = 5
#probabilidade de fracasso
pf = 1-p
#sucesso P(x) 
x = 5

#fórmula
#P(x) = n! / x!(n-x)! *px *qn-x
P_resultado = (0.75**(5))*(0.25**(5-5))


print(P_resultado)
