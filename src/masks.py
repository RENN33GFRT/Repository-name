import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('utils.log', encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    try:
        card_number_str = str(card_number)
        logger.info("Проверяем номер карты на наличие букв")
        for i in card_number_str:
            if i.isalpha():
                logger.error(f"Некорректный номер карты: {card_number_str}")
                return "Error"
        logger.info("Проверка на нужную длину строки")
        if len(card_number_str) == 16:
            return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        else:
            logger.error("Некорректная длина номера карты")
            return "Error"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


def get_mask_account(account_number: str) -> str:

    try:
        account_number_str = str(account_number)
        logger.info("Проверка на длину строки и на наличие букв в номере счёта")
        if not account_number_str.isdigit():
            logger.error("Некорректный номер счета, есть символы кроме цифр")
            return "Error"
        else:
            if len(account_number_str) == 20:
                return "**" + account_number_str[-4:]
            else:
                logger.error("Некорректная длина счёта")
                return "Error"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


print(get_mask_account("12345123451234512345"))
print(get_mask_card_number("1234123412341234"))
