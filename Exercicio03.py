#Leia do teclado a temperatura em Celsius e imprima o equivalente em Fahrenheit.
#(Fórmula: (X ºC × 9/5) + 32

celsius = float(input("Infome a temperatura em Celsius:  "))
calculoFahrenheit = (celsius * 9/5) + 32

print("A temperatura",celsius,"Cº corresponde a",calculoFahrenheit, "Fº")
