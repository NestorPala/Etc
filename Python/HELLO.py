# SAMPLE CODE BY NestorPala


NO_NAME = "no"
NO_AGE = -1
ADULT_AGE = 18
MAX_AGE = 125


def greeting(name: str = None) -> None:
    return "Sin nombre no te puedo saludar :(" if not name else f"Hola {name}!"


def is_adult(age: int = 0) -> bool:
    if age > MAX_AGE:
        raise Exception(f"La edad no puede ser mayor a {MAX_AGE} años")
        
    return age >= ADULT_AGE


def data_is_invalid(data: list) -> bool:
    return len(data) != 2 or not data[1].isnumeric()


def get_user_personal_data() -> set:
    data = list()

    while data_is_invalid(data):
        data = input("Hola, ingresa tu nombre y tu edad (ejemplo: carlos 43)  >>>  ")
        if data == NO_NAME: return (NO_NAME, NO_AGE)
        data = data.split(" ")

    current_user = data[0]
    age = int(data[1])

    return (current_user, age)


def main() -> None:
    current_user, age = get_user_personal_data()

    if current_user.lower() == NO_NAME:
        print(greeting())
        return
    
    print(greeting(name=current_user.capitalize()))

    if age != NO_AGE:
        print("Ya sos mayor de edad." if is_adult(age) else "Todavia no sos mayor de edad.")


main()
