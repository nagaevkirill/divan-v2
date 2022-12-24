import json
import ENV

def count_goods(cat, date):
    try:
        with open(f'{ENV.DATA_PATH}\\daily_parse\\{date}_{cat}.json', 'r', encoding='UTF-8') as file:
            data = json.load(file)
            return 'Количество товаров: ' + str(len(data))
    except Exception:
        return 'Нет данных за это число'