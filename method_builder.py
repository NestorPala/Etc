
def separator_to_camelCase(string: str, separator: str = " ", is_method_name: bool = True) -> str:
    capitalized = list(map(lambda s: s.capitalize(), string.split(separator)))
    if is_method_name: capitalized[0] = capitalized[0].lower()
    return "".join(capitalized)


def build_method(method_name: str) -> str:
    return f"@Test\npublic void {method_name}()\n{{\n\n}}\n"


def main() -> None:
    method_names = [
        "no se puede crear un jugador con posicion inicial invalida",
        "no se puede crear un jugador con un vehiculo inicial invalido",
        'la puntuacion inicial del jugador es cero puntos',
    ]

    for m in method_names:
        print(build_method(separator_to_camelCase(m)))
        print(2 * '\n')


main()
