import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def addition(num_1: float, num_2: float) -> float:
    return num_1 + num_2


def subtraction(num_1: float, num_2: float) -> float:
    return num_1 - num_2


def multiplication(num_1: float, num_2: float) -> float:
    return num_1 * num_2


def division(num_1: float, num_2: float) -> float:
    return num_1 / num_2


operations = {
    "1": (addition, 'Dodaję'),
    "2": (subtraction, 'Odejmuję'),
    "3": (multiplication, 'Mnożę'),
    "4": (division, 'Dzielę')
}


if __name__ == "__main__":
    operator = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, "
                     "4 Dzielenie: ")
    num_1 = float(input("Podaj pierwszą liczbę: "))
    num_2 = float(input("Podaj drugą liczbę: "))
    logging.info(f"{operations[operator][1]} {num_1} i {num_2}.")
    outcome = operations[operator][0](num_1, num_2)
    logging.info(f"Wynik to {outcome}.")


# TODO 5: Sprawdzaj, czy podana wartość na pewno jest liczbą.
# TODO 6: W wypadku mnożenia i dodawania daj użytkownikowi możliwość wpisania większej ilości argumentów niż tylko dwa,
#         np. możesz dodać do siebie trzy i więcej liczb.
