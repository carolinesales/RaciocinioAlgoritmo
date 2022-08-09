#Escreva um algoritmo em Python para calcular o valor, em reais, que deve ser pago por um cliente de uma locadora de carros. Sabe se que:
#a) O valor de locação de cada carro é 100,00 reais;
#b) O cliente pode locar um único carro por vários dias.

carroValor = 100.0
dias = int(input("Informe por quantos dias o carro será alugado: "))

valorTotal = carroValor * dias

print("O valor total é de: R$ " + str(valorTotal))
