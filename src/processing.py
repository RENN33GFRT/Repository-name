from typing import Any


def filter_by_state(list_of_dicts: list[Any], state: str = "EXECUTED") -> list[Any]:
    """Проверяет значение в словарях на заданное и если оно совпадает то, выводит его"""
    correct_list = []
    for num_dict in range(0, len(list_of_dicts) - 1):
        if list_of_dicts[num_dict]["state"] == state:
            correct_list.append(list_of_dicts[num_dict])
    return correct_list


def sort_by_date(list_of_dicts: list[Any], sorting_direct: bool = True) -> list[Any]:
    """Сортирует список по датам в словарях по убывание(по умолчанию)"""
    return sorted(list_of_dicts, key=lambda x: x.get("date"), reverse=sorting_direct)


