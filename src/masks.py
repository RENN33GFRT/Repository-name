def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты по правилу XXXX XX** **** XXXX."""
    card_number_str = str(card_number)
    for i in card_number_str:
        if i.isalpha():
            return "Error"
    if len(card_number_str) == 16:
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    else:
        return "Error"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета по правилу **XXXX."""
    account_number_str = str(account_number)
    if len(account_number_str) == 20 and account_number_str.isdigit():
        return "**" + account_number_str[-4:]
    else:
        return "Error"
