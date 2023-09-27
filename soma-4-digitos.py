num = int(input("Qual é o número? "))
num_milhar = num // 1000
rest1 = num % 1000

num_centena = rest1 // 100
rest2 = rest1 % 100

num_dezena = rest2 // 10
rest3 = rest2 % 10

num_unidade = rest3
print(num_milhar, num_centena, num_dezena, num_unidade)
print(num_milhar + num_centena + num_dezena + num_unidade)
