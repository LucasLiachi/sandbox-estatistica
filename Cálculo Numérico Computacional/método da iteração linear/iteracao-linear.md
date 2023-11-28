A iteração linear é um método numérico utilizado para encontrar o ponto fixo de uma função, que pode ser usado para estimar a raiz de uma função.

O ponto fixo de uma função f(x) é um valor x* que satisfaz a equação f(x*) = x*. Em outras palavras, é um valor para o qual a aplicação repetida da função f(x) resulta no mesmo valor.

Para usar a iteração linear para encontrar o ponto fixo de uma função f(x), siga os passos abaixo:

Escreva a função f(x) na forma x = g(x), em que g(x) é uma função que pode ser iterada. Em outras palavras, resolva a equação f(x) = x para obter x = g(x).

Escolha um valor inicial x0.

Calcule o próximo valor na iteração, xn+1, usando a equação xn+1 = g(xn).

Repita o passo 3 até que a diferença entre xn+1 e xn seja menor que uma tolerância pré-definida.

O valor final xn é o ponto fixo de f(x), que pode ser usado como uma estimativa para a raiz da função.

Vale lembrar que a escolha do valor inicial x0 pode afetar a convergência do método. Portanto, é importante escolher um valor próximo da raiz desejada. Além disso, a escolha da função g(x) também pode afetar a convergência do método. Uma boa escolha para g(x) é uma função que tenha uma derivada contínua e cujo valor absoluto da derivada seja menor que 1 em uma vizinhança da raiz.

Neste exemplo, a função f(x) é definida como cos(x) - 5x + 1 e a função g(x) é definida como (cos(x) + 1)/5, que pode ser obtida resolvendo a equação f(x) = x para obter x = g(x). O valor inicial x0 é definido como 0.5 e a tolerância é definida como 1e-6. A iteração linear é realizada para encontrar o ponto fixo de g(x), que é usado como uma estimativa para a raiz da função f(x). Finalmente, o valor da raiz é impresso na tela.

Lembre-se de que é importante verificar se a função g(x) escolhida satisfaz as condições de convergência da iteração linear. Além disso, para esta função específica, é importante garantir que os valores de x estejam em radianos.


____________________________


Para usar o método da iteração linear, primeiro precisamos isolar a raiz da equação em um intervalo [a, b]. Sabemos que a equação de Kepler é uma função periódica, portanto, podemos escolher um intervalo de comprimento 2π. Para simplificar, vamos escolher o intervalo [0, 2π].

Agora, precisamos transformar a equação em uma forma x = g(x) para poder usar o método da iteração linear. Podemos rearranjar a equação para obter:

x = M + E * sen(x)

Então, podemos definir:

g(x) = M + E * sen(x)

Agora, precisamos escolher um valor inicial x0 no intervalo [0, 2π] e aplicar a iteração:

xi = g(xi-1)

Continuamos a iterar até que a diferença entre xi e xi-1 seja menor ou igual à tolerância especificada. A diferença pode ser medida usando a norma L2.

Para garantir a convergência, precisamos verificar se a derivada de g(x) em relação a x é menor que 1 em módulo no intervalo [0, 2π]. Podemos calcular a derivada:

g'(x) = E * cos(x)

Em módulo, a derivada é sempre menor ou igual a E, que é 0,3 neste caso. Portanto, a condição de convergência é satisfeita.

Agora, podemos escolher um valor inicial x0 e aplicar a iteração até que a diferença entre xi e xi-1 seja menor ou igual a 1e-3. Vamos escolher x0 = 1.5 (no intervalo [0, 2π]).

x1 = g(x0) = 0.672480022

x2 = g(x1) = 0.623578871

x3 = g(x2) = 0.600912187

x4 = g(x3) = 0.596372174

x5 = g(x4) = 0.596210859

x6 = g(x5) = 0.596215155

A partir da sexta iteração, a diferença entre xi e xi-1 é menor ou igual a 1e-3. Portanto, o número mínimo de iterações necessárias para determinar a raiz da equação dada com uma tolerância de 1e-3 é 6.