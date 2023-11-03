import requests
import json
import time

from collections import Counter  # удобный подсчет колличества


def get_items(steam_id, app_id):
    url = f"http://steamcommunity.com/inventory/{steam_id}/{app_id}/2?l=english&count=100"

    response = requests.get(url)
    data = json.loads(response.text)
    list_inventory = []

    if response.status_code == 200:
        all_price = 0.00
        items_assets = data['assets']

        classids = [item['classid'] for item in items_assets]  # считаем повторения каждого классаид предмета
        classid_counts = Counter(classids)

        items_descriptions = data['descriptions']
        for item in items_descriptions:  # перебираем все предметы в дескриптионе
            item_name = item['market_hash_name']
            item_classid = item['classid']

            time.sleep(2) #время задержки пере запросом,чтобы стим не банил айпи
            url_price = f"https://steamcommunity.com/market/priceoverview/?currency=1&appid={app_id}&market_hash_name={item_name}"
            response_price = requests.get(url_price)
            data_price = json.loads(response_price.text)
            if response_price.status_code == 200 or response_price.status_code == 500:
                if response_price.status_code == 500:
                    item_price = "Нет цены"
                else:
                    item_price = data_price['median_price']
                for classid, count in classid_counts.items():  # перебираем все предметы в фссутс
                    if classid == item_classid:  # сравниваем классид в ассетс и в
                        if item_price == "Нет цены":
                            all_price += 0
                        else:
                            all_price += float(count) * float(item_price[1:])
                        list_inventory.append(f"{item_price}|{item_name}|{classid}|{count}\n")
            else:
                list_inventory.append(
                    f"Произошла ошибка при запросе к API Steam market. Ошибка стим - {response_price.status_code}")
        list_inventory.append(f"Стоимость инвентаря - ${all_price}, на вывод - ${all_price * 0.67}")

    else:
        list_inventory.append(f"Произошла ошибка при запросе к API Steam. Ошибка стим - {response.status_code}")

    return list_inventory


# Замените значения на свои ключ API и Steam ID
api_key = "9B05F7EA801303764424859454D44E62"
steam_id = "76561199490909718"
app_id = "440"
