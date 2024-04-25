"""
### Sobre

Faça um Programa que peça dois
números e mostre o maior deles.

### Entrada

Digite um número:<br>
Digite outro número:<br>
O maior é:
"""

numero = int(input("Digite um número: "))
outro_numero = int(input("Digite outro número: "))

if (numero > outro_numero):
    print(f"O número {numero} é maior que {outro_numero}")
elif (numero < outro_numero):
    print(f"O número {outro_numero} é maior que {numero}")
else:
    print(f"O números são iguais")
