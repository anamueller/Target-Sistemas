import math
faturamento = {"SP": 67836.43, 
                "RJ": 36678.66,
                "MG": 29229.88,
                "ES": 27165.48,
                "Outros": 19849.53
            }

print("O percentual de representação que cada estado teve dentro do valor total mensal da distribuidora")
total = sum(faturamento.values())
for k, fat in faturamento.items():
    percentual = fat/total * 100
    print(k,":", round(percentual, 2),"%")