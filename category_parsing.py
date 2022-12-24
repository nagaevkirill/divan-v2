import json
import requests
import time
import ENV


def parse_category(cat_name, url, min_discount):
    response = requests.get(url + '&page=1')
    data_response = response.json()['data']

    total_pages = data_response['pageTotalCount']
    product_dict = []

    print(f'start collect category {cat_name}')

    for i in range(1, total_pages+1):
        response = requests.get(url=f'{url}&page={i}')
        data_response = response.json()['data']
        products = data_response['products']

        for item in products:
            if int(item['price']['discount']) > min_discount:
                product_card = {
                    'id': item['id'],
                    'name': item['name'],
                    'categoryName': item['categoryName'],
                    'isActive': item['isActive'],
                    'link': f"https://divan.ru{item['link']}",
                    'price': item['price'],
                    'image': item['images'][0]['src']
                }

                product_dict.append(product_card)

    print(f'finish collect category {cat_name}')

    with open(f'{ENV.DAILY_PATH}/{time.strftime("%d%m%Y")}_{cat_name}.json', 'w', encoding='utf-8') as file:
        json.dump(product_dict, file, indent=4, ensure_ascii=False)


def product_mapping(file_source, file_new):
    with open(f'{ENV.DAILY_PATH}/{file_new}', 'r', encoding='utf-8') as file_temp:
        temp_file = json.load(file_temp)
    with open(f'{ENV.DAILY_PATH}/{file_source}', 'r', encoding='utf-8') as file_last:
        last_file = json.load(file_last)

    id_dict_last = []
    id_dict_temp = []

    for item in temp_file:
        id_dict_temp.append(item['id'])
    for item in last_file:
        id_dict_last.append(item['id'])

    diff = set(id_dict_temp) - set(id_dict_last)
    with open(f'{ENV.DAILY_PATH}/default.log', 'a', encoding='utf-8') as file_log:
        file_log.write(time.strftime("%H%M%S-%d%m%Y")+'\n')
        if str(diff) == 'set()':
            file_log.write('There is no new goods \n')

        else:
            file_log.write(str(diff) + '\n')


parse_category('divany-i-kresla', 'https://proxy.divan.ru/backend/category/get-products?slug=divany-i-kresla&isInit=true', 0)
parse_category('krovati-i-matrasy', 'https://proxy.divan.ru/backend/category/get-products?slug=krovati-i-matrasy&isInit=true', 0)
parse_category('skafy-i-stellazi', 'https://proxy.divan.ru/backend/category/get-products?slug=skafy-i-stellazi&isInit=true', 0)
parse_category('komody-i-tumby', 'https://proxy.divan.ru/backend/category/get-products?slug=komody-i-tumby&isInit=true', 0)
parse_category('stoly-i-stulya', 'https://proxy.divan.ru/backend/category/get-products?slug=stoly-i-stulya&isInit=true', 0)
parse_category('kovry-i-tekstil', 'https://proxy.divan.ru/backend/category/get-products?slug=kovry-i-tekstil&isInit=true', 0)
parse_category('svet', 'https://proxy.divan.ru/backend/category/get-products?slug=svet&isInit=true', 0)

