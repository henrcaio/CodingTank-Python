"""Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
sempre será a soma dos 2 valores anteriores(ex: 0, 1, 1, 2, 3, 5, 8, 13...), 
escreva um programa na linguagem que desejar onde, informado um número, ele 
calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número 
informado pertence ou não a sequência."""

n1 = 0
n2 = 1
sum = 0
count = 0
belonging = False
userInput = int(input("Type a number: "))

while n1 <= userInput:
    sum = n1 + n2
    n1 = n2
    n2 = sum
    count += 1

    if n1 == userInput:
        belonging = True

if belonging == True:
    print("Number belongs the Fibonacci sequence")
else:
    print("Number does NOT belong the Fibonacci sequence")
