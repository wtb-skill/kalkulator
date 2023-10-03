import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def addition(*args: float) -> float:
    return sum(args)


def subtraction(*args: float) -> float:
    result = 0
    for number in args:
        result -= number
    return result


def multiplication(*args: float) -> float:
    result = 1
    for number in args:
        result *= number
    return result


def division(*args: float) -> float:
    result = args[0]
    for number in args[1:]:
        result /= number
    return result


operations = {
    "1": (addition, 'Dodaję'),
    "2": (subtraction, 'Odejmuję'),
    "3": (multiplication, 'Mnożę'),
    "4": (division, 'Dzielę')
}


def collect_numbers():
    numbers = []
    while True:
        try:
            user_input = input("Podaj liczbę: ")
            if user_input.lower() == 'done':
                break
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            logging.info("To nie jest liczba!")
    return numbers


def define_operation():
    while True:
        user_input = input(
            "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        if user_input in ['1', '2', '3', '4']:
            break  # Break out of the loop if a valid number is entered
        else:
            logging.info("To nie jest odpowiednia liczba! Podaj 1, 2, 3 lub 4.")
    return user_input


def print_numbers(numbers):
    message = str(numbers[0])
    for number in numbers[1:]:
        message += f" i {number}"
    return message


if __name__ == "__main__":
    operator = define_operation()
    numbers = collect_numbers()
    if operator == '4' and any(number == 0 for number in numbers[1:]):  # division by 0
        logging.info("Nie można dzielić przez 0.")
        numbers = collect_numbers()
    logging.info(f"{operations[operator][1]} {print_numbers(numbers)}.")
    outcome = operations[operator][0](*numbers)
    logging.info(f"Wynik to {outcome}.")

