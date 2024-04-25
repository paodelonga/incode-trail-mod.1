"""
### Sobre

Faça um Programa que leia
três números diferentes e
mostre o maior deles.
"""

n1 = int(input("Digite o 1° número : "))
n2 = int(input("Digite o 2° número : "))
n3 = int(input("Digite o 3° número : "))

if n1 > n2:
    if n1 > n3:
        print(f"O maior número é o 1°: {n1}")
    elif n3 > n1:
        print(f"O maior número é o 3°: {n3}")
else:
    if n2 > n3:
        print(f"O maior número é o 2°: {n2}")
    elif n3 > n2:
        print(f"O maior número é o 3°: {n3}")
