#Escreva um algoritmo em Python para calcular a idade de alguém, sabendo seu ano de nascimento.

anoAtual = int(input("Digite o Ano Atual: "))
anoNascimento = int(input("Digite o seu Ano de Nascimento: "))

calculoIdade = anoAtual - anoNascimento

print("Sua idade é: " + str(calculoIdade))