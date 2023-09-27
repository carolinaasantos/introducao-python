A = []
B = []

digitado = 0
while digitado != "Acabei" or digitado != "acabei":
  digitado = (input("Digite um número: (caso tenha acabado, digite 'Acabei') "))
  if digitado == "Acabei" or digitado == "acabei":
    break
  else:
    digitado = int(digitado)
  A.append(digitado)
  B.append(digitado)
quantidade = len(A)
j = 0
i = 0
temp = 0
while i < quantidade - 1:
  j = i
  while j < (quantidade - 1):
    if A[i] > A[1 + j]:
      temp = A[1 + j]
      A[1 + j] = A[i]
      A[i] = temp
    j += 1
  i += 1
print(f"""A lista digitada foi: {B}
A lista na ordem crescente é: {A}""")
