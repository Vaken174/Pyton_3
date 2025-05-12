from typing import List, Union, TypeVar

ElementType = TypeVar('ElementType', int, float, str)# Создаем переменную, которая может быть int, float, str

def multiply_items(
        elements: List[ElementType],# Список
        multiplier: Union[int, float] = 2# Множитель
) -> List[ElementType]:# Новый список с множителем
    
    return [element * multiplier for element in elements]# Каждый элемент умножается на множитель


def run_program() -> None:# Основная функция для обработки ввода и вывода
    
    user_input = input("Введите числа через пробел: ").strip()
    
    
    if not user_input:# Проверка на пустой ввод
        print("Вы ничего не ввели")
        return

    try:
        # Преобразовываем ввод в список
        # Целые в инт остальные в флоат
        number_list = [int(num) if num.isdigit() else float(num) for num in user_input.split()]
    except ValueError:
        print("Ошибка: вводите только числа!")# Ошибка
        return

    # Запрос множителя с обработкой значения по умолчанию
    multiplier_input = input("Введите множитель (по умолчанию 2): ").strip()
    multiplier_value = 2 if not multiplier_input else float(multiplier_input)

    # Вызов основной функции умножения
    function_result = multiply_items(number_list, multiplier_value)
    print(f"Результат (функция): {function_result}")

    # Альтернативная реализация через lambda-функцию
    multiply_with_lambda = lambda items, factor: [item * factor for item in items]
    lambda_result = multiply_with_lambda(number_list, multiplier_value)
    print(f"Результат (лямбда-функция): {lambda_result}")


if __name__ == "__main__":
    run_program()