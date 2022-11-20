def from_shop_to_store(shop, store, request):
    if shop.items[request.product] < request.amount:
        print(f'Нет такого количества {request.product} на в магазине')
    elif store.get_free_space() < request.amount:
        print("На складе недостаточно места")
    else:
        store.add(request.product, request.amount)
        shop.remove(request.product, request.amount)


def from_store_to_shop(shop, store, request):
    if store.items[request.product] < request.amount:
        print(f'Нет такого количества {request.product} на складе')
    elif request.product not in shop.items.keys() and len(shop.items) == 5:
        print("Предел количества товаров")
    elif shop.get_free_space() < request.amount:
        print("В магазине недостаточно свободного места")
    else:
        shop.add(request.product, request.amount)
        store.remove(request.product, request.amount)
