PRODUCCIONES = {
    1: (
        "CONSULTA",
        [
            "SELECT",
            "IDENTIFICADOR",
            "FROM",
            "IDENTIFICADOR",
            "PUNTO_Y_COMA"
        ]
    )
}

PRODUCCIONES = {
    1: (
        "CONSULTA",
        [
            "SELECT",
            "COLUMNAS",
            "FROM",
            "IDENTIFICADOR",
            "PUNTO_Y_COMA"
        ]
    ),

    2: (
        "COLUMNAS",
        ["IDENTIFICADOR"]
    ),

    3: (
        "COLUMNAS",
        [
            "IDENTIFICADOR",
            "COMA",
            "IDENTIFICADOR"
        ]
    )
}


ACTION = {

    (0, "SELECT"): ("SHIFT", 1),

    (1, "IDENTIFICADOR"): ("SHIFT", 2),

    (2, "FROM"): ("REDUCE", 2),
    (2, "COMA"): ("SHIFT", 3),

    (3, "IDENTIFICADOR"): ("SHIFT", 4),

    (4, "FROM"): ("REDUCE", 3),

    (5, "FROM"): ("SHIFT", 6),

    (6, "IDENTIFICADOR"): ("SHIFT", 7),

    (7, "PUNTO_Y_COMA"): ("SHIFT", 8),

    (8, "$"): ("REDUCE", 1),

    (9, "$"): ("ACCEPT",)
}


GOTO = {

    (1, "COLUMNAS"): 5,

    (0, "CONSULTA"): 9
}


def parser_lr(tokens):

    pila = [0]
    indice = 0

    print("\nANALISIS SINTACTICO LR")
    print("=" * 100)

    print(
        f"{'PILA':<40}"
        f"{'ENTRADA':<40}"
        f"{'ACCION'}"
    )

    while True:

        estado = pila[-1]
        simbolo = tokens[indice]

        accion = ACTION.get((estado, simbolo))

        print(
            f"{str(pila):<40}"
            f"{str(tokens[indice:]):<40}"
            f"{accion}"
        )

        if accion is None:

            print("\nERROR SINTACTICO")
            return False

        tipo = accion[0]

        if tipo == "SHIFT":

            nuevo_estado = accion[1]

            pila.append(simbolo)
            pila.append(nuevo_estado)

            indice += 1

        elif tipo == "REDUCE":

            num_prod = accion[1]

            izquierda, derecha = PRODUCCIONES[num_prod]

            for _ in range(len(derecha) * 2):
                pila.pop()

            estado = pila[-1]

            pila.append(izquierda)

            nuevo_estado = GOTO[(estado, izquierda)]

            pila.append(nuevo_estado)

        elif tipo == "ACCEPT":

            print("\nCADENA ACEPTADA")
            return True