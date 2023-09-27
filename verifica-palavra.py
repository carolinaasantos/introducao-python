def verif_presente (palavra, lista):
  presente = False
  comprimento = len(lista)
  i = 0
  while i < comprimento:
    if lista[i] == palavra:
      print(f"A palavra {palavra} está presente na lista, sendo o {i + 1}º elemento")
      presente = True
      break
    i += 1
  if presente == False:
    lista.append(palavra)
    print(f"""A palavra '{palavra}' não estava na lista, mas agora está!
{lista}""")

lista = []
quantidade = int(input("Quantas palavras sua lista terá? "))
j = 0
while j < quantidade:
  lista.append(input("Digite uma palavra: "))
  j += 1
palavra = input("Digite a palavra que quer verificar se está na lista: ")
verif_presente (palavra, lista)
