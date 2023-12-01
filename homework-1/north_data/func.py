import csv


def read_csv(path):
    """
    Функция читает из csv и преобразует список словарей в список картежей
    """
    with open(path, 'r', encoding="utf-8") as csv_file:
        csv_data: csv.DictReader = csv.DictReader(csv_file)
        csv_data_list = list(csv_data)
        db_list = []

        for i, line_dict in enumerate(csv_data_list):
            line = line_dict.values()
            tuple_line = tuple(line)
            db_list.insert(i, tuple_line)
    return db_list