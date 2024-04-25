operadores = [
    ("+", int.__add__, "ADICAO"),
    ("-", int.__sub__, "SUBTRACAO"),
    ("*", int.__mul__, "MULTIPLICACAO"),
    ("÷", int.__truediv__, "DIVISAO"),
]

for operador in operadores:
    print(f"=== TABUADA DE {operador[2]} ===")
    for a in range(1, 11):
        for b in range(1, 11):
            if operador[0] == "÷":
                print(f"{a}{operador[0]}{b} = {operador[1](a, b):.3f}")
            else:
                print(f"{a}{operador[0]}{b} = {operador[1](a, b)}")
        print("")
    print("")
