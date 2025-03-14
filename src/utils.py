import json
import os
import logging


logger = logging.getLogger('utils')
file_handler = logging.FileHandler("utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(file_path):
    logger.debug(f"Запущена функция get_transactions с file_path: {file_path}")

    if not os.path.isfile(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    logger.debug(f"Успешно прочитано {len(data)} транзакций из файла.")
                    return data
                else:
                    logger.warning(f"Файл содержит не список: {file_path}")
                    return []
            except json.JSONDecodeError:
                logger.error(f"Ошибка декодирования JSON в файле: {file_path}",
                             exc_info=True)
                return []
    except Exception as e:
        logger.error(f"Произошла ошибка при работе с файлом: {file_path}", exc_info=True)
        return []


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "..", "data", "transactions.json")
    transactions = get_transactions(path)
    if transactions:
        print(f"Найдено {len(transactions)} транзакций.")
    else:
        print("Транзакции не найдены.")
