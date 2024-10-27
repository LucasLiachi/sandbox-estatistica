import numpy as np

# Dados das cidades
desvios_1 = np.array([4, 6, 3, 3, 2, 4])
medias_1 = np.array([91, 93, 92, 94, 96, 95])

desvios_2 = np.array([6, 5, 7, 6, 8, 8])
medias_2 = np.array([91, 105, 102, 117, 121, 129])

desvios_3 = np.array([8, 6, 7, 9, 8, 8])
medias_3 = np.array([140, 106, 101, 101, 132, 129])

# Função para calcular desvio relativo médio
def desvio_relativo_medio(desvios, medias):
    desvios_relativos = desvios / medias
    return np.mean(desvios_relativos)

# Calcular desvios relativos médios
desvio_relativo_medio_1 = desvio_relativo_medio(desvios_1, medias_1)
desvio_relativo_medio_2 = desvio_relativo_medio(desvios_2, medias_2)
desvio_relativo_medio_3 = desvio_relativo_medio(desvios_3, medias_3)

# Ordenação por homogeneidade
homogeneidade = sorted([
    ('Cidades < 400k habitantes', desvio_relativo_medio_1),
    ('Cidades 400k-1M habitantes', desvio_relativo_medio_2),
    ('Cidades > 1M habitantes', desvio_relativo_medio_3)
], key=lambda x: x[1])

# Resultado
print("Ordem de Homogeneidade (do mais homogêneo ao menos homogêneo):")
for i, (grupo, valor) in enumerate(homogeneidade):
    print(f"{i+1}º: {grupo}")
