from analizador_lexico import (
    analizador_lexico,
    convertir_tokens,
    tabla_simbolos
)

from parser_lr import parser_lr


with open("Entrada.txt", "r", encoding="utf-8") as archivo:
    codigo = archivo.read()


tokens = analizador_lexico(codigo)

print("\nTOKENS ENCONTRADOS")
print("=" * 70)

for i, t in enumerate(tokens, start=1):

    print(
        f"{i:<3}"
        f"{t['lexema']:<15}"
        f"{t['token']:<20}"
        f"L{t['linea']} C{t['columna']}"
    )


print("\nTABLA DE SIMBOLOS")
print("=" * 40)

for nombre, info in tabla_simbolos.items():

    print(
        f"{nombre:<20}"
        f"{info['primera_aparicion']}"
    )


tokens_parser = convertir_tokens(tokens)

print("\nTOKENS PARA EL PARSER")
print(tokens_parser)

resultado = parser_lr(tokens_parser)

if resultado:
    print("\nCONSULTA SQL VALIDA")
else:
    print("\nCONSULTA SQL INVALIDA")