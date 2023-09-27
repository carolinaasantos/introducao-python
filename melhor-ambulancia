from math import sqrt
i = 0
ambulancia_x = []
ambulancia_y = []
distancia = 0
menor = 10000

ponto_x = int(input("Qual é o X da vítima? "))
ponto_y = int(input("Qual é o Y da vítima? "))
quantidade_ambul = int(input("Qual é a quantidade de ambulâncias? "))

while i < quantidade_ambul:
  ambulancia_x.insert(i, int(input(f"Qual é a coordenada X da ambulância {i+1}? ")))
  ambulancia_y.insert(i, int(input(f"Qual é a coordenada Y da ambulância {i+1}? ")))
  i += 1

i = 0
while i < quantidade_ambul:
  distancia = sqrt((ponto_x - ambulancia_x[i])**2 + (ponto_y - ambulancia_y[i])**2)
  print(distancia)
  if distancia < menor:
    menor = distancia
    melhor_ambul = i + 1
    menor_x = ambulancia_x[i]
    menor_y = ambulancia_y[i]
  i += 1

print(f"A melhor ambulância é a {melhor_ambul}, a qual apresenta coordenadas ({menor_x}, {menor_y}) e está a uma distância de {menor}.")
