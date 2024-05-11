Uma fábrica de autopeças possuía duas linhas de produção idênticas para seu principal produto. Os gestores precisavam aumentar a capacidade de produção dessas linhas para atender a um novo contrato de fornecimento com uma grande montadora que passaria a vigorar em 6 meses. Eles precisavam decidir entre a alternativa de investir em duas máquinas novas, uma para cada linha de produção, ou se seria suficiente otimizar a produção fazendo um retrofitting das máquinas existentes, um novo layout para o fluxo da produção e um maior número de funcionários dedicados a cada linha. Eles também queriam ter maior flexibilidade em controlar a taxa de produção.

Os gestores pediram a uma jovem engenheira de produção, recém-contratada, para ajudá-los na análise dessas alternativas. Essa jovem engenheira, após alguns testes, desenvolveu o seguinte modelo: 
y = 0,17a +29,12b + 21,19c - 15,74bc
em que :
a = velocidade da máquina (rpm)
b = Layout (antigo = 0 e novo = 1 )
c = número de funcionários (atual = 0 e maior = 1)
y = volume de produção da linha (peças / hora)
Com base no modelo descrito, responda às seguintes perguntas:

**1) Quais foram as variáveis estudadas?**
a = velocidade da máquina (rpm)
b = Layout (0 para antigo, 1 para novo)
c = Número de funcionários (0 para atual, 1 para maior)
y = Volume de produção da linha (peças/hora)

**2) Qual o tipo de cada variável, quantitativa ou qualitativa? Se quantitativa, qual sua unidade de medida? Se qualitativa, que níveis ou classes podem assumir?**
a = Maquina sendo uma variável quantitativa contínua medida em rpm.
b = Layout sendo uma variável quantitativa discreta, em binário.
c = Número de funcionários uma variável quantitativa contínua, pois representa a quantidade de funcionários disponíveis.
y = Volume de produção uma variável quantitativa contínua pois representa o volume de produção.

**3) Como pode esse modelo de regressão linear múltipla ser usado para fazer predição de volume de produção de cada linha da fábrica?**
O modelo busca prever o volume de produção da linha com base nos valores das variáveis x1, x2, e x3. Ao fornecer os valores para essas variáveis, pode ser usado para estimar o volume de produção esperado.

**4) Reflita sobre situações similares em que você poderia aplicar essa mesma técnica (regressão linear múltipla) para gerar conhecimento a partir de dados. Descreva brevemente uma dessas situações que você pensou, identifique cada uma das variáveis de entrada e a variável resposta, descreva o tipo de cada uma delas (se quantitativa ou qualitativa) e forneça suas unidades de medida (se quantitativas) ou seus níveis ou classes (se qualitativas).**
Um exeplo possivel seria em uma cadeia de restaurantes onde desejam entender seu tempo de preparo.
Com base nas variáveis temperatura ambiente (a), a presença de uma promoção especial (b), e o número de funcionários na equipe de cozinha (c) afetam o tempo de preparo de um prato específico. Com objetivo é prever o tempo de preparo com base nessas variáveis:
a (Temperatura): Quantitativa contínua (em graus Celsius).
b (Promoção): Qualitativa nominal (0 para sem promoção, 1 para com promoção).
c (Número de funcionários): Quantitativa discreta.
Variável resposta: Tempo de preparo do prato (minutos), quantitativa contínua.

