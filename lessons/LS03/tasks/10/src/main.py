"""
### Sobre

Faça um Programa que leia três
números diferentes e mostre-os
em ordem decrescente.
"""

n1 = int(input("Digite o 1° número : "))
n2 = int(input("Digite o 2° número : "))
n3 = int(input("Digite o 3° número : "))

if n3 < n2:
    if n2 < n1:
        print(n3, n2, n1)
    elif n1 < n2:
        print(n3, n1, n2)
elif n2 < n3:
    if n1 < n2:
        print(n1, n2, n3)
    elif n2 < n1:
        print(n2, n1, n3)
