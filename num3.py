from typing import Any, List, Tuple, Dict, Union


def function_name(
        mode: str,
        flag: bool,
        *arguments: Any,
        **named_arguments: Any
) -> Union[List[int], str]:
    """
    Обрабатывает аргументы в зависимости от параметров mode и flag.

    Параметры:
        mode (str): Определяет режим обработки:
            - "args" - обработка позиционных аргументов
            - "kwargs" - обработка именованных аргументов
        flag (bool): Флаг, определяющий тип обработки для режима "args":
            - True: фильтрация целых чисел
            - False: конкатенация всех аргументов
        *arguments: Произвольные позиционные аргументы
        **named_arguments: Произвольные именованные аргументы

    Возвращает:
        Union[List[int], str]:
            - Для mode="args" и flag=True: список целых чисел
            - Для mode="args" и flag=False: строку из всех аргументов
            - Для mode="kwargs": строку с описанием пар ключ-значение

    Исключения:
        ValueError: Если параметр mode имеет недопустимое значение
    """
    numbers_list: List[int] = []
    output_string: str = ""

    if mode == "args":
        if flag:
            for item in arguments:
                if isinstance(item, int):
                    numbers_list.append(item)
            return numbers_list
        else:
            for item in arguments:
                output_string += f"{item}"
            return output_string
    elif mode == "kwargs":
        for key, value in named_arguments.items():
            output_string += ("Key: {}, Value: {}; ".format(key, value))
        return output_string
    else:
        raise ValueError("Error for mode")