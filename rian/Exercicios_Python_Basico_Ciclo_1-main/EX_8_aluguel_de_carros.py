# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dias = int(input("qual foi a quantidade de km percorrido pelo carro de aluguel: "))
km = float(input("quantos dias ele foi alugado :"))
custo_dias = 60.0
km_por_rodada = 0.15
preco = (dias* custo_dias) + (km * km_por_rodada)
print(f"voce andou {km}km por {dias} dias, entao o preco a pagar é {preco}")