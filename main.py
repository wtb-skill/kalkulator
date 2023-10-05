import logging
from typing import Callable

logging.basicConfig(level=logging.DEBUG, format='\n%(asctime)s %(message)s')


def addition(a: float, b: float, *args: float) -> float:
    """
    Calculate the sum of two or more numbers.

    This function takes two or more floating-point numbers as arguments and returns
    their sum. The first two arguments, 'a' and 'b', are added together, and any
    additional numbers provided in the variable-length argument 'args' are also
    added to the result.

    :param a: The first floating-point number.
    :param b: The second floating-point number.
    :param args: Variable-length arguments containing additional numbers to be added.
    :return: The sum of 'a', 'b', and any additional numbers provided in 'args'.
    """
    result = a + b
    for number in args:
        result += number
    return result


def subtraction(a: float, b: float, *args: float) -> float:
    """
    Calculate the result of subtracting one or more numbers from a base value.

    This function takes two or more floating-point numbers as arguments. It subtracts
    the second argument 'b' from the first argument 'a' and then subtracts any
    additional numbers provided in the variable-length argument 'args' from the
    intermediate result. The final result is returned as a float.

    :param a: The base floating-point number from which subtraction begins.
    :param b: The second floating-point number to subtract from 'a'.
    :param args: Variable-length arguments containing additional numbers to subtract.
    :return: The result of subtracting 'b' and any additional numbers in 'args' from 'a'.
    """
    result = a - b
    for number in args:
        result -= number
    return result


def multiplication(a: float, b: float, *args: float) -> float:
    """
    Calculate the product of two or more numbers.

    This function takes two or more floating-point numbers as arguments. It multiplies
    the first argument 'a' by the second argument 'b' and then multiplies the result
    by any additional numbers provided in the variable-length argument 'args'. The final
    product is returned as a float.

    :param a: The first floating-point number to be multiplied.
    :param b: The second floating-point number to be multiplied.
    :param args: Variable-length arguments containing additional numbers to be multiplied.
    :return: The product of 'a', 'b', and any additional numbers in 'args'.
    """
    result = a * b
    for number in args:
        result *= number
    return result


def division(a: float, b: float, *args: float) -> float:
    """
    Calculate the result of dividing one or more numbers by a base value.

    This function takes two or more floating-point numbers as arguments. It divides
    the first argument 'a' by the second argument 'b' and then divides the result by
    any additional numbers provided in the variable-length argument 'args'. The final
    result is returned as a float.

    :param a: The base floating-point number to be divided.
    :param b: The divisor, a floating-point number.
    :param args: Variable-length arguments containing additional numbers to be divided.
    :return: The result of dividing 'a' by 'b' and any additional numbers in 'args'.
    """
    result = a / b
    for number in args:
        result /= number
    return result


operations: dict[str, tuple[Callable[..., float], str]] = {
    "1": (addition, 'Dodaję'),
    "2": (subtraction, 'Odejmuję'),
    "3": (multiplication, 'Mnożę'),
    "4": (division, 'Dzielę')
}


def collect_numbers() -> list[float]:
    """
    This function prompts the user to input numbers one at a time. It continues
    accepting numbers until the user enters 'done' and at least two numbers have
    been provided. If the user enters non-numeric input, an error message is
    displayed, and they are prompted to enter another number.

    :return: A list of float numbers entered by the user.
    """
    numbers = []
    print("Podaj kolejno liczby, na których chcesz wykonać działanie. Aby zakończyć podawanie wpisz 'done'.")
    while True:
        user_input = input("Podaj liczbę: ")
        if user_input.lower() == 'done':
            if len(numbers) >= 2:  # user must input at least 2 numbers
                break
            else:
                logging.info("Musisz wprowadzić co najmniej 2 liczby. Podaj kolejną liczbę.")
                continue
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            logging.info("To nie jest liczba! Podaj kolejną liczbę.")
    return numbers


def define_operation() -> str:
    """
    Prompt the user to select a mathematical operation and return the chosen option.

    This function displays a menu to the user, asking them to select a mathematical
    operation by entering a corresponding number:

    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division

    The function waits until the user enters a valid option (1, 2, 3, or 4) and
    returns the chosen option as a string.

    :return: A string representing the chosen operation ('1', '2', '3', or '4').
    """
    while True:
        user_input = input(
            "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        if user_input in ['1', '2', '3', '4']:
            break  # Break out of the loop if a valid number is entered
        else:
            logging.info("To nie jest odpowiednia liczba! Podaj 1, 2, 3 lub 4.")
    return user_input


def print_numbers(list_of_numbers: list[float]) -> str:
    """
    Create a string representation of a list of numbers, separated by the letter 'i'.

    This function takes a list of float numbers and generates a string representation
    where the numbers are concatenated together with the letter 'i' in between them.
    For example, if the input list_of_numbers is [1.0, 2.5, 3.7], the function
    will return '1.0 i 2.5 i 3.7'.

    :param list_of_numbers: A list of floats to be concatenated.
    :return: A string of numbers separated by 'i'.
    """
    message = str(list_of_numbers[0])
    for number in list_of_numbers[1:]:
        message += f" i {number}"
    return message


if __name__ == "__main__":
    operator = define_operation()
    numbers = collect_numbers()

    while operator == '4' and any(number == 0 for number in numbers[1:]):  # division by 0
        logging.info("Nie można dzielić przez 0.")
        numbers = collect_numbers()

    logging.info(f"{operations[operator][1]} {print_numbers(numbers)}.")
    outcome = operations[operator][0](*numbers)
    logging.info(f"Wynik to {outcome}.")


