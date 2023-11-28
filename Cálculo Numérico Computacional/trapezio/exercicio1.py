t = [0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200] # tempos em segundos
v = [20, 22, 23, 25, 30, 31, 32, 40, 45, 50, 65] # velocidades em km/h

n = len(t) - 1 # número de intervalos
h = (t[-1] - t[0]) / n # tamanho de cada intervalo

areas = []
for i in range(n):
    v1 = v[i]
    v2 = v[i+1]
    t1 = t[i]
    t2 = t[i+1]
    area = (v1 + v2) * (t2 - t1) / 2
    areas.append(area)

distancia = sum(areas) * 1000/3600 # convertendo de km/h para m/s

print(f"Aproximação da distância percorrida: {distancia:.0f} metros")
