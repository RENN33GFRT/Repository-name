import pandas as pd


def CSV_file_read(file_path):
    """
        Читает данные из CSV файла и возвращает их в виде списка словарей.

        Параметры:
        file_path (str): Путь к CSV файлу, который необходимо прочитать.

        Возвращает:
        list: Список словарей, где каждый словарь представляет собой строку из файла.
              Если файл не найден, возвращает сообщение "Файл не найден".
        """
    try:
        df = pd.read_csv(file_path, delimiter=";")
        fixed_df = df.dropna(how="any")
        list_of_dicts = fixed_df.to_dict(orient="records")
        return list_of_dicts
    except FileNotFoundError:
        return "Файл не найден"


def XLSX_file_read(file_path):
    """
       Читает данные из Excel файла и возвращает их в виде списка словарей.

       Параметры:
       file_path (str): Путь к Excel файлу, который необходимо прочитать.

       Возвращает:
       list: Список словарей, где каждый словарь представляет собой строку из файла.
             Если файл не найден, возвращает сообщение "Файл не найден".
       """
    try:
        df = pd.read_excel(file_path)
        fixed_df = df.dropna(how="any")
        list_of_dicts = fixed_df.to_dict(orient="records")
        return list_of_dicts
    except FileNotFoundError:
        return "Файл не найден"
