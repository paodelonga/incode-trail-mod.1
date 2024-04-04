# Kalzone 8.90
# Suco 5.00
# Hamburguer = 20.00
# Refrigerante = 4.00

print("""
========= CARDAPIO =========
N | NOME          | PRECO     | TIPO            |
1 | Kalzone       | R$4.00    | PRINCIPAL       |
2 | Hamburguer    | R$20.00   | PRINCIPAL       |
3 | Refrigerante  | R$5.00    | ACOMPANHAMENTO  |
4 | Suco          | R$8.90    | ACOMPANHAMENTO  |
============================
""")

# Entrada
per_deseja_pedido = "sim" # input("Gostaria de fazer um pedido? ")

# Inicia o pedido
if per_deseja_pedido == "sim" :
  print("INSTRUCAO: Faca o pedido utilizando o N do item\n")

  # Bloco de pedidos/pratos principais
  pedido_principal = str(input("Qual o prato principal? "))
  qtd_principal = int(input(f"Qual a quantidade de pratos Nº{pedido_principal}? "))

  per_outro_principal = str(input("Deseja outro prato principal? "))
  if per_outro_principal == "sim":
    outro_principal = str(input("Qual o outro prato principal? "))
    qtd_outro_principal = int(input(f"Qual a quantidade de pratos Nº{outro_principal}? "))

    pedido_principal = pedido_principal + outro_principal

  print(f"{pedido_principal} {qtd_principal}")
  print(f"{outro_principal} {qtd_outro_principal}")

  # Bloco de acompanhamentos/outros
  per_pedido_acomp = str(input("Deseja acompanhamento? "))
  if per_pedido_acomp == "sim":

    acomp_principal = str(input("Qual o acompanhamento? "))
    qtd_acomp_principal = int(input(f"Qual a quantidade do acompanhamento Nº{acomp_principal}? "))

    per_outro_acomp = str(input("Deseja outro acompanhamento? "))
    if per_outro_acomp == "sim":
      outro_acomp = str(input("Qual o outro acompanhamento? "))
      qtd_outro_acomp = int(input(f"Qual a quantidade do acompanhamento Nº{outro_acomp}? "))

      acomp_principal = acomp_principal + outro_acomp

    print(f"{acomp_principal} {qtd_acomp_principal}")
    print(f"{outro_acomp} {qtd_outro_acomp}")

