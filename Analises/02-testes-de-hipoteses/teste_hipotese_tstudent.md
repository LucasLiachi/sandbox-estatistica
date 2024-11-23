## Porque buscar a hipótese nula

A busca pela hipótese nula é fundamental em testes estatísticos, como o teste t de Student, por várias razões:

1. **Base para comparação**: A hipótese nula fornece uma base para comparação. Ela afirma uma condição neutra, como igualdade de médias entre amostras, permitindo que qualquer diferença observada seja atribuída à variação aleatória ou ao acaso.

2. **Teste de significância**: A partir da hipótese nula, é possível determinar se as diferenças observadas entre as amostras são estatisticamente significativas. Isso ajuda a evitar conclusões precipitadas e a garantir que as conclusões sejam baseadas em evidências sólidas.

3. **Controle de erro tipo I**: A rejeição incorreta da hipótese nula (erro tipo I) pode levar a conclusões falsas. Portanto, é importante estabelecer um nível de significância a priori e tomar decisões com base nesse limite, evitando conclusões enganosas.

4. **Interpretação dos resultados**: Ao manter a hipótese nula como ponto de referência, podemos interpretar os resultados do teste de hipóteses de forma mais precisa, entendendo se há evidências suficientes para rejeitá-la em favor da hipótese alternativa.

Portanto, ao realizar um teste de hipóteses com o teste t de Student, é crucial formular e buscar a hipótese nula, como exemplificado no problema dado. Isso proporciona uma estrutura sólida para análise estatística e interpretação dos resultados.

## Passos para análise com t-student

### Passo 1: Formulação das Hipóteses

- **Hipótese Nula (H0)**: As médias das duas amostras são iguais.
- **Hipótese Alternativa (H1)**: As médias das duas amostras são diferentes.

### Passo 2: Coleta de Dados

Suponha que você tenha os seguintes dados:

- Amostra A: 
  - Tamanho da amostra (n1) = 20
  - Média da amostra (x̄1) = 15
  - Desvio padrão da amostra (s1) = 3

- Amostra B:
  - Tamanho da amostra (n2) = 25
  - Média da amostra (x̄2) = 18
  - Desvio padrão da amostra (s2) = 4

### Passo 3: Escolha do Nível de Significância (α)

Vamos escolher um nível de significância de 5%, o que significa que estamos dispostos a aceitar um erro de tipo I de 5%.

### Passo 4: Cálculo do Estatístico de Teste

O estatístico de teste t pode ser calculado usando a fórmula:

\[ t = \frac{{(\bar{x}_1 - \bar{x}_2)}}{{\sqrt{\frac{{s_1^2}}{{n_1}} + \frac{{s_2^2}}{{n_2}}}}} \]


### Passo 5: Decisão

Compare o valor de t calculado com o valor crítico da distribuição t de Student com os graus de liberdade apropriados (calculados como n1 + n2 - 2). Se o valor de t estiver dentro da região crítica (ou seja, for maior que o valor crítico positivo ou menor que o valor crítico negativo), rejeitamos a hipótese nula.

### Cálculos:

Substituindo os valores conhecidos na fórmula, temos:

\[ t = \frac{{(15 - 18)}}{{\sqrt{\frac{{3^2}}{{20}} + \frac{{4^2}}{{25}}}}} \]

\[ t = \frac{{-3}}{{\sqrt{\frac{{9}}{{20}} + \frac{{16}}{{25}}}}} \]

Calculando os valores dentro da raiz:

\[ t = \frac{{-3}}{{\sqrt{0.45 + 0.64}}} \]

\[ t = \frac{{-3}}{{\sqrt{1.09}}} \]

\[ t \approx \frac{{-3}}{{1.044}}} \]

\[ t \approx -2.87 \]

Agora, consultando a tabela da distribuição t de Student com \( n_1 + n_2 - 2 = 20 + 25 - 2 = 43 \) graus de liberdade e um nível de significância de 5%, encontramos o valor crítico de t para um teste de duas caudas. Suponha que seja \( t_{\alpha/2, \, n_1+n_2-2} = \pm 2.015 \) (valor aproximado).

Como \( t \) é menor do que \( -t_{\alpha/2, \, n_1+n_2-2} \), rejeitamos a hipótese nula.

Então, podemos concluir que há evidências estatísticas para sugerir que as médias das duas amostras são diferentes.

