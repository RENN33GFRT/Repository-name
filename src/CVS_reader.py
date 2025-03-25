import pandas as pd


def CSV_file_read(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=";")
        fixed_df = df.dropna(how="any")
        list_of_dicts = fixed_df.to_dict(orient="records")
        return list_of_dicts
    except FileNotFoundError:
        return "Файл не найден"


def XLSX_file_read(file_path):
    try:
        df = pd.read_excel(file_path)
        fixed_df = df.dropna(how="any")
        list_of_dicts = fixed_df.to_dict(orient="records")
        return list_of_dicts
    except FileNotFoundError:
        return "Файл не найден"


print(CSV_file_read("..\\data\\transactions.csv"))
# print(XLSX_file_read('..\\data\\transactions_excel.xlsx'))