# Exercício prático elaborado para entender a disciplina

Um exemplo de função mais complexa para um treinador de basquete pode ser a função que descreve a relação entre o tempo de jogo e o número de pontos marcados pelo jogador, levando em consideração a taxa de acerto de arremessos e a habilidade do jogador em se movimentar e criar oportunidades de arremesso.

Essa função pode ser escrita como f(t) = a * t^3 + b * t^2 + c * t + d, onde a, b, c e d são constantes que dependem das habilidades do jogador e da dinâmica do jogo. Encontrar as raízes dessa função usando o método de bisseção pode ser útil para determinar o momento em que o jogador atingiu um determinado número de pontos, ou para encontrar o ponto de inflexão da curva de desempenho do jogador. Nesse caso, é difícil encontrar a solução analítica para a função, e o método de bisseção é uma opção viável para encontrar as raízes com precisão.

As constantes de habilidades de jogadores e dinâmica de jogo que podem afetar a relação entre o tempo de jogo e o número de pontos marcados podem incluir:

## Taxa de acerto de arremessos: 
Esta é uma medida da precisão do jogador ao arremessar a bola. Jogadores com alta taxa de acerto tendem a marcar mais pontos em menos tempo. Por exemplo, uma constante a alta pode ser usada para representar um jogador com alta taxa de acerto.

## Habilidade de movimentação: 
Esta é uma medida da habilidade do jogador em se movimentar pela quadra e criar oportunidades de arremesso. Jogadores com alta habilidade de movimentação tendem a ter mais chances de arremesso e, portanto, marcar mais pontos em menos tempo. Uma constante b alta pode ser usada para representar um jogador com alta habilidade de movimentação.

## Defesa do time adversário: 
A dinâmica do jogo pode ser influenciada pela habilidade defensiva do time adversário. Jogadores que enfrentam times defensivos fortes podem ter mais dificuldade em marcar pontos, enquanto jogadores que enfrentam times defensivos fracos podem marcar mais pontos em menos tempo. Uma constante c pode ser usada para representar o efeito da defesa do time adversário.

## Estratégia de jogo: 
A dinâmica do jogo também pode ser influenciada pela estratégia de jogo do treinador e do time. Por exemplo, se o treinador usa uma estratégia de jogo ofensiva que incentiva os jogadores a arremessar mais rapidamente, os jogadores podem marcar mais pontos em menos tempo. Uma constante d pode ser usada para representar o efeito da estratégia de jogo.

É importante ressaltar que a escolha dessas constantes pode variar de acordo com o treinador, o time e a liga em que o jogo está sendo disputado. Além disso, a modelagem matemática do desempenho de um jogador em um jogo de basquete pode ser bastante complexa e envolver mais variáveis do que as mencionadas acima.

# Exemplo

Suponha que o treinador queira encontrar o momento em que o jogador marcou 20 pontos em um jogo de basquete, utilizando a função f(t) = a * t^3 + b * t^2 + c * t + d, onde a, b, c e d são constantes que dependem das habilidades do jogador e da dinâmica do jogo.

Para utilizar o método de bisseção, o treinador precisa definir um intervalo [t1, t2] que contenha a raiz (o momento em que o jogador marcou 20 pontos) e que seja possível de ser dividido em subintervalos menores. Suponha que o jogo tem duração de 45 minutos e que o treinador decide que a raiz está no intervalo [10, 30] minutos de jogo.

O próximo passo é calcular o valor da função f(t) nos extremos do intervalo:

f(10) = a * 10^3 + b * 10^2 + c * 10 + d
f(30) = a * 30^3 + b * 30^2 + c * 30 + d

Suponha que esses valores sejam f(10) = 1000 e f(30) = 4000.

O método de bisseção consiste em dividir o intervalo [10, 30] em subintervalos menores e avaliar o valor da função no ponto médio de cada subintervalo, até que o valor da função esteja próximo de zero (ou do valor desejado, no caso do treinador). Por exemplo, o treinador pode dividir o intervalo [10, 30] em dois subintervalos:

[10, 20], com ponto médio t = 15
[20, 30], com ponto médio t = 25
O valor da função no ponto médio de cada subintervalo é:

f(15) = a * 15^3 + b * 15^2 + c * 15 + d
f(25) = a * 25^3 + b * 25^2 + c * 25 + d

Suponha que esses valores sejam f(15) = 2000 e f(25) = 3500.

Como o valor de f(15) é menor que o valor desejado de 20 pontos, o treinador pode descartar o intervalo [10, 15] e continuar a busca no intervalo [15, 20]. O processo de divisão do intervalo e cálculo do valor da função no ponto médio pode ser repetido até que o valor de f(t) esteja próximo de zero (ou do valor desejado, no caso do treinador).

Por exemplo, o treinador pode dividir o intervalo [15, 20] em dois subintervalos:

[15, 17.5], com ponto médio t = 16.25
[17.5, 20], com ponto médio t = 18.75
O valor da função no ponto médio de cada subintervalo é:

f(16.25) = a * 16.25^3 + b * 16.25^2 + c * 16.25 + d
f(18.75) = a * 18.75^3 + b * 18.75^2 + c * 18.75 + d