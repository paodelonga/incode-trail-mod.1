print("""
===================== CARDAPIO =====================
| N | NOME          | PRECO     | TIPO             |
|---|---------------|-----------|------------------|
| 1 | Kalzone       | R$4.00    | PRINCIPAL        |
| 2 | Hamburguer    | R$20.00   | PRINCIPAL        |
| 3 | Refrigerante  | R$5.00    | ACOMPANHAMENTO   |
| 4 | Suco          | R$8.90    | ACOMPANHAMENTO   |
====================================================
 > Ao fazer o pedido escreva o N do item desejado <
""")


# Inicializando as variaveis
valor_pedido = float()
per_deseja_pedido = str()

### Primeiro prato
pedido_principal = str()
qtd_principal = int()

### Outro prato
per_outro_principal = str()
outro_principal = str()
qtd_outro_principal = int()
principal_completo = str()

### Primeiro acompanhamento
per_pedido_acomp = str()
acomp_principal = str()
qtd_acomp_principal = int()

### Outro acompanhamento
per_outro_acomp = str()
outro_acomp = str()
qtd_outro_acomp = int()
acomp_completo = str()


# Entrada/pergunta primaria
per_deseja_pedido = input("Gostaria de fazer um pedido? ")


# Inicia o processo de pedido
if per_deseja_pedido == "sim" :

  # Bloco de pedidos/pratos principais
  pedido_principal = input("Qual o prato principal desejado? ")
  qtd_principal = int(input(f"Qual a quantidade de pratos Nº{pedido_principal}? "))

  per_outro_principal = input("Deseja outro prato principal? ")
  if per_outro_principal == "sim":
    outro_principal = input("Qual o outro prato principal? ")
    qtd_outro_principal = int(input(f"Qual a quantidade de pratos Nº{outro_principal}? "))

    principal_completo = pedido_principal + outro_principal
    # print(f"{outro_principal} {qtd_outro_principal}")

  # print(f"{pedido_principal} {qtd_principal}")

  # Bloco de acompanhamentos/outros
  per_pedido_acomp = input("Deseja acompanhamento? ")
  if per_pedido_acomp == "sim":

    acomp_principal = input("Qual o acompanhamento desejado? ")
    qtd_acomp_principal = int(input(f"Qual a quantidade do acompanhamento Nº{acomp_principal}? "))

    per_outro_acomp = input("Deseja outro acompanhamento? ")
    if per_outro_acomp == "sim":
      outro_acomp = input("Qual o outro acompanhamento? ")
      qtd_outro_acomp = int(input(f"Qual a quantidade do acompanhamento Nº{outro_acomp}? "))

      acomp_completo = acomp_principal + outro_acomp
      # print(f"{outro_acomp} {qtd_outro_acomp}")

    # print(f"{acomp_principal} {qtd_acomp_principal}")

  # Processamento dos dados
  ### Primeiro prato
  if len(pedido_principal) > 0:
    if pedido_principal == "1":
      valor_pedido = float(qtd_principal * 4.0)
    elif pedido_principal == "2":
      valor_pedido = float(qtd_principal * 20.0)
    else:
      print(f"O prato de Nº{pedido_principal} não existe."  )

    ### Segundo prato
    if len(outro_principal) > 0:
      if outro_principal == "1":
        valor_pedido = float(valor_pedido + (qtd_outro_principal * 4.0))
      elif outro_principal == "2":
        valor_pedido = float(valor_pedido + (qtd_outro_principal * 20.0))
      else:
        print(f"O prato de Nº{pedido_principal} não existe."  )

    ### Primeiro acompanhamento
    if len(acomp_principal) > 0:
      if acomp_principal == "3":
        valor_pedido = float(valor_pedido + (qtd_acomp_principal * 5.00))
      elif acomp_principal == "4":
        valor_pedido = float(valor_pedido + (qtd_acomp_principal * 8.90))
      else:
        print(f"O acompanhamento de Nº{acomp_principal} não existe."  )

      ### Segundo prato
      if len(outro_acomp) > 0:
        if outro_acomp == "3":
          valor_pedido = float(valor_pedido + (qtd_outro_acomp * 5.00))
        elif outro_acomp == "4":
          valor_pedido = float(valor_pedido + (qtd_outro_acomp * 8.90))
        else:
          print(f"O acompanhamento de Nº{acomp_principal} não existe."  )

  if valor_pedido > 0:
    print(f"\nO valor do pedido é de R${valor_pedido}")
