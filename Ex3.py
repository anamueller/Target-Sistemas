faturamentos =[1,2,3,4,5,6]
diassuperior=0
media = sum(faturamentos)/len(faturamentos) #media mensal, pegando o tamanho ja excluimos os dias que nao tiveram faturamento
for dias in range(len(faturamentos)):
    if faturamentos[dias]>media:
        diassuperior = diassuperior+1
print("Abaixo temos o menor e maior valor de faturamento ocorrido em um dia do mês,e o número de dias no mês em que o valor de faturamento diário foi superior à média mensal.")
print(min(faturamentos), max(faturamentos), diassuperior)