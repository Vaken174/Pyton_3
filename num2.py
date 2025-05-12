import math
from typing import List, Union

Number = Union[int, float]


class MathOperations:
    """Класс с математическими операциями"""

    @staticmethod
    def add_numbers(first_number: Number, second_number: Number) -> Number:
        """Складывает два числа"""
        if not all(isinstance(number, (int, float)) for number in [first_number, second_number]):
            raise ValueError("Нужны числа!")
        return first_number + second_number

    @staticmethod
    def subtract_numbers(minuend: Number, subtrahend: Number) -> Number:
        """Вычитает второе число из первого"""
        MathOperations._validate_numbers(minuend, subtrahend)
        return minuend - subtrahend

    @staticmethod
    def multiply_numbers(multiplicand: Number, multiplier: Number) -> Number:
        """Умножает два числа"""
        MathOperations._validate_numbers(multiplicand, multiplier)
        return multiplicand * multiplier

    @staticmethod
    def divide_numbers(dividend: Number, divisor: Number) -> Number:
        """Делит первое число на второе"""
        MathOperations._validate_numbers(dividend, divisor)
        if divisor == 0:
            raise ZeroDivisionError("Нельзя делить на ноль!")
        return dividend / divisor

    @staticmethod
    def raise_to_power(base: Number, exponent: Number) -> Number:
        """Возводит число в степень"""
        MathOperations._validate_numbers(base, exponent)
        return base ** exponent

    @staticmethod
    def calculate_factorial(integer_number: int) -> int:
        """Вычисляет факториал"""
        if not isinstance(integer_number, int):
            raise TypeError("Нужно целое число")
        if integer_number < 0:
            raise ValueError("Факториал только для положительных")
        return math.factorial(integer_number)

    @staticmethod
    def calculate_sine(angle: Number) -> float:
        """Вычисляет синус угла"""
        MathOperations._validate_numbers(angle)
        return math.sin(angle)

    @staticmethod
    def calculate_median(number_sequence: List[Number]) -> Number:
        """Находит медиану списка"""
        if not number_sequence:
            raise ValueError("Список пуст")
        MathOperations._validate_numbers(*number_sequence)
        sorted_numbers = sorted(number_sequence)
        sequence_length = len(sorted_numbers)
        middle_index = sequence_length // 2
        return sorted_numbers[middle_index] if sequence_length % 2 else (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2

    @staticmethod
    def _validate_numbers(*numbers_to_check: Number) -> None:
        """Проверяет, что все аргументы - числа"""
        for number in numbers_to_check:
            if not isinstance(number, (int, float)):
                raise TypeError("Все аргументы должны быть числами")


def display_menu():
    """Показывает меню операций"""
    print("\nДоступные операции:")
    operations = [
        "1. Сложение",
        "2. Вычитание",
        "3. Умножение",
        "4. Деление",
        "5. Степень",
        "6. Факториал",
        "7. Синус",
        "8. Медиана",
        "exit - Выход"
    ]
    print("\n".join(operations))
    print("-" * 20)


def get_number_from_user(prompt_message: str) -> Number:
    """Получает число от пользователя"""
    while True:
        try:
            user_input = input(prompt_message)
            return float(user_input) if "." in user_input else int(user_input)
        except ValueError:
            print("Ошибка! Введите число")


def get_number_list_from_user(prompt_message: str) -> List[Number]:
    """Получает список чисел"""
    while True:
        try:
            input_values = input(prompt_message).split()
            return [float(value) if "." in value else int(value) for value in input_values]
        except ValueError:
            print("Ошибка! Вводите только числа через пробел")


def execute_calculator():
    """Запускает калькулятор"""
    display_menu()

    while True:
        user_choice = input("\nВыберите операцию: ").strip().lower()

        if user_choice in ("exit", "quit", "q"):
            print("Работа завершена")
            break

        try:
            if user_choice == "1":
                first_num, second_num = get_number_from_user("Первое число: "), get_number_from_user("Второе число: ")
                calculation_result = MathOperations.add_numbers(first_num, second_num)
            elif user_choice == "2":
                first_num, second_num = get_number_from_user("Уменьшаемое: "), get_number_from_user("Вычитаемое: ")
                calculation_result = MathOperations.subtract_numbers(first_num, second_num)
            elif user_choice == "3":
                first_num, second_num = get_number_from_user("Первый множитель: "), get_number_from_user("Второй множитель: ")
                calculation_result = MathOperations.multiply_numbers(first_num, second_num)
            elif user_choice == "4":
                first_num, second_num = get_number_from_user("Делимое: "), get_number_from_user("Делитель: ")
                calculation_result = MathOperations.divide_numbers(first_num, second_num)
            elif user_choice == "5":
                first_num, second_num = get_number_from_user("Основание: "), get_number_from_user("Степень: ")
                calculation_result = MathOperations.raise_to_power(first_num, second_num)
            elif user_choice == "6":
                input_num = get_number_from_user("Число: ")
                calculation_result = MathOperations.calculate_factorial(int(input_num))
            elif user_choice == "7":
                input_angle = get_number_from_user("Угол в радианах: ")
                calculation_result = MathOperations.calculate_sine(input_angle)
            elif user_choice == "8":
                numbers = get_number_list_from_user("Числа через пробел: ")
                calculation_result = MathOperations.calculate_median(numbers)
            else:
                print("Неизвестная команда!")
                continue

            print(f"Результат: {calculation_result}")
            print("-" * 20)

        except Exception as error:
            print(f"Ошибка: {error}")
            print("-" * 20)


if __name__ == "__main__":
    execute_calculator()