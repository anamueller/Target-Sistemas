import faulthandler
import json

f = open('dados.json')
json_file = json.load(f)
valores = []
diassuperior=0
dias = 0 

for i in range(len(json_file)):
    for val in json_file[i].values():
        if val>31 or val==0:
            valores.append(val)

for i in range(len(valores)):
    if(valores[i]!=0):
        dias = dias + 1

media = sum(valores)/dias

for i in range(len(valores)):
    if valores[i]>media:
        diassuperior = diassuperior+1

print("A média do mês foi de", media, "e o número de dias com faturamente igual a zero foram", len(valores)-dias)
print("O menor e maior valor de faturamento ocorridos no mês foram",min(valores),"e",max(valores),"e o número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi", diassuperior)