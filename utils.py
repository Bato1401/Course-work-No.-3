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
    return data[:5]  # Возвращает 5 отсортированных транзакций


def get_data_output(data):
    """
    Функция выводит данные в требуемом формате
    """
    operations = []
    for row in data:
        date_ = row["date"]
        first_line = f'{date_[8:10]}.{date_[5:7]}.{date_[:4]} {row["description"]}'  # первая строка
        card_name = ''.join([x for x in row['from'] if x.isalpha()])
        card_num = ''.join([x for x in row['from'] if x.isdigit()])
        account_name = ''.join([x for x in row['to'] if x.isalpha()])
        account_num = ''.join([x for x in row['to'] if x.isdigit()])
        second_line = f'{card_name} {card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]} ' \
                      f'- > {account_name} **{account_num[-4:]}'  # вторая строка
        third_line = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'  # третья строка
        operations.append(f'''{first_line}\n{second_line}\n{third_line}''')
    return operations
