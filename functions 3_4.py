shop_list = list()
price_item = 0
check_number = 0


def add_item(title, price):
    global shop_list
    global price_item
    price_item += price
    shop_list.append(f"{title} - {price}")


def print_receipt():
    global shop_list
    global check_number
    global price_item
    if shop_list:
        check_number += 1
        itog = 0
        print(f'Чек {check_number}. Всего предметов: {len(shop_list)}')
        for elem in shop_list:
            itog += price_item
            print(elem)
        print(f'Итого: {itog}')
        print('-----')
        itog = 0
        shop_list.clear()
        price_item = 0
