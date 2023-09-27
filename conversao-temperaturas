def calcula_temp_farenheit (temp_celsius):
  temp_farenheit = (9*temp_celsius + 160)/5
  return temp_farenheit

def calcula_temp_kelvin (temp_celsius):
  temp_kelvin = temp_celsius + 273
  return temp_kelvin

opcao = int(input("""Escolha a opção desejada: 
1. Conversão de Celsius para Farenheit.
2. Conversão de Celsius para Kelvin.
"""))

temp_celsius = float(input("Qual é a temperatura em graus Celsius? "))

if opcao == 1:
  temperatura = calcula_temp_farenheit(temp_celsius) 
  print(f"A temperatura {temp_celsius}°C em Farenheit é {temperatura}°F")
else:
  temperatura = calcula_temp_kelvin(temp_celsius)
  print(f"A temperatura {temp_celsius}°C em Kelvin é {temperatura}K")
