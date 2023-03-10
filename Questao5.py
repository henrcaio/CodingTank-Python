"""Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua 
preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""

userInput = input("Write a sentence: ")
count = 0

# Same as using "len(userInput)"
for char in userInput:
    count + 1

for char in userInput[::-1]:
    print(char, end="")
