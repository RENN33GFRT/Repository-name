import os

import requests
from dotenv import load_dotenv



def get_transaction_amount(transaction_info, currency="RUB"):
    code = transaction_info.get("operationAmount").get("currency").get("code")
    amount = transaction_info.get("operationAmount").get("amount")
    if code == currency:
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={1}"
        load_dotenv()
        API_KEY = os.getenv("API_KEY")
        headers = {"apikey": f"{API_KEY}"}
        response = requests.get(url, headers=headers)
        return response.json().get("result")

    response = requests.get(url, headers=headers)

    result = response.text
    return result

