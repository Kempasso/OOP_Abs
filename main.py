from classes import Request, Store, Shop
from utils import from_shop_to_store, from_store_to_shop

store = Store({"огурец": 1, "помидор": 1, "лук": 1})
shop = Shop({"огурец": 3, "помидор": 2, "лук": 7})
while True:
    user_input: list = input().split(' ')
    request = Request(user_input)
    if request.fromm == 'магазин':
        from_shop_to_store(shop, store, request)
    else:
        from_store_to_shop(shop, store, request)
    print(store.items)
    print(shop.items)
