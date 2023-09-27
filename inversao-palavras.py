nome_invertido = []

palavra = input("Digite a palavra: ")
quantidade = len(palavra)
palavra_invertida = ""

j = quantidade - 1
k = 0
while j >= 0:
  nome_invertido.append(palavra[j])
  palavra_invertida = palavra_invertida + nome_invertido[k]
  k += 1
  j -= 1

print(f"A palavra '{palavra}' escrita ao contrário é '{palavra_invertida}'")
