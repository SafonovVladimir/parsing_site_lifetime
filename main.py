import requests
import datetime
import csv


def parsing():
    filedate = datetime.datetime.now().strftime("%d_%m_%d")
    url = 'https://www.lifetime.plus/api/analysis2'
    response = requests.get(url)
    data = response.json()
    categories = data['categories']
    result = []

    for c in categories:
        c_name = c.get('name')
        c_items = c.get('items')
        for item in c_items:
            item_name = item.get('name').strip()
            item_price = item.get('price')
            item_days = item.get('days')
            item_bio = item.get('biomaterial').strip()
            item_desc = item.get('description').strip()
            item_pg = item.get('preparationGuide').strip()

            result.append([c_name, item_name, item_price, item_days, item_bio, item_desc, item_pg])

    with open(f'result_{filedate}.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Категорія',
                'Аналіз',
                'Вартість',
                'Кількість днів',
                'Біоматеріал',
                'Опис',
                'Підготовка'
            )
        )
        writer.writerows(result)


def main():
    parsing()


if __name__ == '__main__':
    main()
