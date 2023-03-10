"""Dado o valor de faturamento mensal de uma distribuidora, detalhado por 
estado:

SP – R$67.836, 43
RJ – R$36.678, 66
MG – R$29.229, 88
ES – R$27.165, 48
Outros – R$19.849, 53

Escreva um programa na linguagem que desejar onde calcule o percentual de 
representação que cada estado teve dentro do valor total mensal da distribuidora."""

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
outros = 19849.53

total = SP + RJ + MG + ES + outros

print("Rounded Percentages")
print("SP =", round((SP/total)*100, 2), "%")
print("RJ =", round((RJ/total)*100, 2), "%")
print("MG =", round((MG/total)*100, 2), "%")
print("ES =", round((ES/total)*100, 2), "%")
print("Outros =", round((outros/total)*100, 2), "%")
