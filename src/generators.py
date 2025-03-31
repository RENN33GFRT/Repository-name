from typing import Any

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

def filter_by_currency_json(list_of_transactions: list[Any], currency: str):
    """Функция которая фильтрует список json по заданной валюте
    (то есть в списке остаются только те транзакции у которых нужная валюта)"""
    my_list = []
    for i in list_of_transactions:
        if i.get("operationAmount").get("currency").get("code") == currency:
            my_list.append(i)
    return my_list


def filter_by_currency_csvxlsx(list_of_transactions: list[Any], currency: str):
    """Функция которая фильтрует список csv и xlsx по заданной валюте
    (то есть в списке остаются только те транзакции у которых нужная валюта)"""
    my_list = []
    for i in list_of_transactions:
        if i.get("currency_code") == currency:
            my_list.append(i)
    return my_list


def transaction_descriptions(transactions):
    for transaction in transactions:
        if transaction.get("description"):
            yield transaction.get("description")


def card_number_generator(start: int, stop: int):
    if start < 0 or stop > 9999999999999999:
        raise ValueError("Введены неправильные значения")
    else:
        index = start
        number = "0" * (16 - len(str(index))) + str(index)
        for i in range(start, stop + 1):
            yield f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
            index += 1
            number = "0" * (16 - len(str(index))) + str(index)
