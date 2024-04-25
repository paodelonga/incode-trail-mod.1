"""
### Sobre

Faça um Programa que calcule o valor final da
conta do restaurante:

| Valor da conta | % do Garcom | Couvert | Por Pessoas |
| :---: | :---: | :---: | :---: |
| Acima de R$100 | - | 1 Pessoa | - |
| De R\$50 a R\$99,99 | 5% | Mais de 1 Pessoa | R\$ Por Pessoa |
| Ate R\$49,99 | 10% | | |

### Entrada

Valor do consumo:
Pessoas na mesa
Valor final:
"""

consumo_mesa = float(input("Qual valor de consumo na sua mesa? "))
pessoas_mesa = int(input("Qual a quantidade de pessoas na sua mesa? "))
valor_garcom = float()
valor_conta = float()

if (pessoas_mesa > 1):
    valor_garcom = (5 * pessoas_mesa)

if (consumo_mesa <= 49.99):
    valor_garcom = ((10 * (consumo_mesa/100)) + valor_garcom)
    valor_conta = (consumo_mesa + valor_garcom)
if (consumo_mesa >= 50 and consumo_mesa <= 99.99):
    valor_garcom = ((5 * (consumo_mesa/100)) + valor_garcom)
    valor_conta = (consumo_mesa + valor_garcom)
if (consumo_mesa >= 100):
    valor_conta = (consumo_mesa + valor_garcom)

print(
    f"Para a quantidade de {pessoas_mesa} pessoas o valor total da conta foi de {valor_conta:.2f} incluindo o adicional de {valor_garcom:.2f} para o Garcom."
)
