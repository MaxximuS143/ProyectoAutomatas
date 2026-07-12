import re

TOKENS = [
    ("PALABRA_CLAVE", r"(?i)\b(SELECT|FROM)\b"),
    ("IDENTIFICADOR", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("COMA", r","),
    ("PUNTO_Y_COMA", r";"),
    ("ESPACIO", r"[ \t\n\r]+"),
]

tabla_simbolos = {}


def analizador_lexico(codigo_fuente):

    posicion = 0
    linea = 1
    columna = 1

    tokens_encontrados = []

    while posicion < len(codigo_fuente):

        match = None

        for token_tipo, patron in TOKENS:

            regex = re.compile(patron)
            match = regex.match(codigo_fuente, posicion)

            if match:

                lexema = match.group(0)

                if token_tipo != "ESPACIO":

                    token_info = {
                        "token": token_tipo,
                        "lexema": lexema,
                        "linea": linea,
                        "columna": columna
                    }

                    tokens_encontrados.append(token_info)

                    if token_tipo == "IDENTIFICADOR":

                        nombre = lexema.lower()

                        if nombre not in tabla_simbolos:
                            tabla_simbolos[nombre] = {
                                "primera_aparicion": f"{linea}:{columna}"
                            }

                saltos = lexema.count("\n")

                if saltos > 0:
                    linea += saltos
                    columna = len(lexema.split("\n")[-1]) + 1
                else:
                    columna += len(lexema)

                posicion = match.end(0)
                break

        if not match:

            print(
                f"ERROR LEXICO: "
                f"{codigo_fuente[posicion]} "
                f"(Linea {linea}, Columna {columna})"
            )

            posicion += 1
            columna += 1

    return tokens_encontrados


def convertir_tokens(tokens):

    resultado = []

    for t in tokens:

        if t["token"] == "PALABRA_CLAVE":
            resultado.append(t["lexema"].upper())
        else:
            resultado.append(t["token"])

    resultado.append("$")

    return resultado