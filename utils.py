import json


def get_data():
    """
    Функция для чтения файла operation.json
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


