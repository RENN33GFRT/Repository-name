def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера карты в формате XXXX XX** **** XXXX.

    :param card_number: Номер карты в виде числа.
    :return: Маска номера карты.
    """
    card_str = str(card_number)
    return f"XXXX XX{card_str[-4:-2]} **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску номера счета в формате **XXXX.

    :param account_number: Номер счета в виде числа.
    :return: Маска номера счета.
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
