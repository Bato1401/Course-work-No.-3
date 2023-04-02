import json


def get_data():
    """
    Функция для чтения файла operation.json
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_filtered_data(data):
    """
    Функция фильтрует данные по заданным параметрам и сохраняет в переменную data
    """
    data = [x for x in data if 'state' in x and 'from' in x and x['state'] == 'EXECUTED']
    return data


def get_last_values(data):
    """
    Функция сортирует отфильтрованные данные по дате и выстраивает на убывание
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
