import re
from collections import Counter, defaultdict


def description_filter(transactions: list, word: str) -> list:
    pattern = re.compile(word, re.IGNORECASE)
    my_list = [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]
    return my_list


def category_count(transactions: list, categories: list) -> dict:
    sorted_dict = defaultdict(list)
    for i in categories:
        sorted_dict[i] = 0

    descriptions = []
    for i in transactions:
        descriptions.append(i.get("description"))

    counted = Counter(descriptions)
    for i in categories:
        sorted_dict[i] = counted[i]

    return dict(sorted_dict)
