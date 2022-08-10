from re import I


texto = input("Escreva a string que deseja inverter: ")
invertido = []
i=1
for caracter in range(len(texto)):
    invertido.append(texto[len(texto)-i])
    i=i+1
print("Palavra invertida:")
print(''.join(invertido))