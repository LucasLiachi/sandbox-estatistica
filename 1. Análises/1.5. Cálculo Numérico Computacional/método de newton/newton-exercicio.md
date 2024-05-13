O método de Newton é um algoritmo utilizado para encontrar as raízes de uma função. A ideia por trás deste método é usar uma aproximação inicial e aplicar a fórmula de Newton-Raphson para obter uma nova aproximação mais precisa a cada iteração.

A fórmula de Newton-Raphson é dada por:

x[n+1] = x[n] - f(x[n])/f'(x[n])

Onde:

x[n] é a aproximação inicial na n-ésima iteração;
x[n+1] é a nova aproximação na (n+1)-ésima iteração;
f(x[n]) é o valor da função f na aproximação inicial x[n];
f'(x[n]) é o valor da derivada de f na aproximação inicial x[n].
Segue abaixo um exemplo de como implementar o método de Newton para encontrar uma raiz da função f(x) = x^3 - 2x - 5:

Escolha uma aproximação inicial x[0];
Calcule f(x[0]) e f'(x[0]);
Calcule a nova aproximação x[1] usando a fórmula de Newton-Raphson:
x[1] = x[0] - f(x[0])/f'(x[0]);
Repita o passo 3 até que a diferença entre x[n+1] e x[n] seja menor que uma tolerância pré-estabelecida.


Neste exemplo, a função newton implementa o método de Newton e recebe como parâmetros a função f, a sua derivada df, a aproximação inicial x0 e a tolerância tol. A função newton retorna a raiz encontrada.

A função f representa a função a ser resolvida e a função df representa a sua derivada. A aproximação inicial é definida como x0 e a tolerância é definida como tol. No exemplo acima, a raiz encontrada da função f é 2.0945514815423265.