"""Cardapio utilizando while"""

print(
    """
 ======== CARDAPIO ========
| N | PRECO   | NOME      |
|---|---------|-----------|
| 1 | R$4.00  | Hotdog    |
| 2 | R$8.50  | Kalzone   |
| 3 | R$20.50 | Hamburger |
| 4 | R$12.50 | X-Salada  |
| 5 | R$10.20 | X-Bacon   |
| 6 | R$2.00  | Fanta     |
| 7 | R$4.50  | Coca-Cola |
| 8 | R$3.15  | Suco      |
============================
"""
)

cardapio = {
    1: {"preco": 4.00, "nome": "Hotdog"},
    2: {"preco": 8.50, "nome": "Kalzone"},
    3: {"preco": 20.50, "nome": "Hamburger"},
    4: {"preco": 12.50, "nome": "X-Salada"},
    5: {"preco": 10.20, "nome": "X-Bacon"},
    6: {"preco": 2.00, "nome": "Fanta"},
    7: {"preco": 4.50, "nome": "Coca-Cola"},
    8: {"preco": 3.15, "nome": "Suco"},
}

valor_pedido = float()

andamento_pedido = True

while andamento_pedido:
    try:
        item_desejado = int(input("Qual o N do item desejado? "))
    except ValueError:
        print("a entrada não é um numeral")
        break

    if item_desejado in cardapio:
        quantidade_item = float(
            input(f"Qual a quantidade de {cardapio[item_desejado]['nome']}? ")
        )
        valor_pedido += cardapio[item_desejado]["preco"] * quantidade_item

        finalizar_pedido = input("Quer finalizar seu pedido? sim/nao ").lower()
        if "sim" in finalizar_pedido:
            print(f"\nO valor total foi: R${valor_pedido:.2f}")
            print("Obrigado pela preferencia :)")
            andamento_pedido = False

    elif item_desejado not in cardapio:
        print(f"ERRO: O numero {item_desejado} nao esta no cardapio.")
        andamento_pedido = False
