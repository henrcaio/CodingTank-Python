"""Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
faça um programa, na linguagem que desejar, que calcule e retorne:

• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
Estes dias devem ser ignorados no cálculo da média;"""

import json

with open("dados.json") as givenFile:
    dados = json.load(givenFile)

lowestValue = 0.0
highestValue = 0.0
average = 0.0
count = 0
days = 0

# Defining average
for i in dados:
    average += i["valor"]
    count += 1
average = average/count

# Defining lowest value
for i in dados:
    if lowestValue <= i["valor"]:
        continue
    else:
        lowestValue = i["valor"]

# Defining highest value
for i in dados:
    if highestValue >= i["valor"]:
        continue
    else:
        highestValue = i["valor"]

# Defining number of days in which the revenue was higher than the average
for i in dados:
    if i["valor"] > average:
        count += 1

print("The lowest value was", lowestValue)
print("The highest value was", highestValue)
print("The daily revenue was higher than the average in", count, "days")
