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

    while True:
        operator = input(
            "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        if operator in ['1', '2', '3', '4']:
            break  # Break out of the loop if a valid number is entered
        else:
            print("To nie jest odpowiednia liczba! Podaj 1, 2, 3 lub 4.")

    while True:
        try:
            number_1 = float(input("Podaj pierwszą liczbę: "))
            break  # Break out of the loop if a valid number is entered
        except ValueError:
            print("To nie jest liczba!")

    while True:
        try:
            number_2 = float(input("Podaj drugą liczbę: "))
            break  # Break out of the loop if a valid number is entered
        except ValueError:
            print("To nie jest liczba!")

    logging.info(f"{operations[operator][1]} {number_1} i {number_2}.")
    outcome = operations[operator][0](number_1, number_2)
    logging.info(f"Wynik to {outcome}.")


# TODO 6: W wypadku mnożenia i dodawania daj użytkownikowi możliwość wpisania większej ilości argumentów niż tylko dwa,
#         np. możesz dodać do siebie trzy i więcej liczb.
