# Resposta
def maior_numero (a, b, c):
  if a > b and a > c:
    maior_numero = a
  elif b > a and b > c:
    maior_numero = b
  elif c > a and c > b:
    maior_numero = c
  else:
    maior_numero = "Não há maior número"
  return maior_numero

def menor_numero (a, b, c):
  if a < b and a < c:
    menor_numero = a
  elif b < a and b < c:
    menor_numero = b
  elif c < a and c < b:
    menor_numero = c
  else:
    menor_numero = "Não há menor número"
  return menor_numero
  
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

num_maior = maior_numero(num1, num2, num3)
num_menor = menor_numero(num1, num2, num3)

print(f"Entre os números {num1}, {num2} e {num3}, o maior deles é {num_maior} e o menor deles é {num_menor}.")
