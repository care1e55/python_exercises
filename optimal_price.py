from collections import defaultdict

storages = defaultdict(dict)
products = defaultdict(list)
result = []


def find_lowest_price(product_id: int, price: int) -> str:
    if not products[product_id]:
        return "-1 -1"
    product_storages = products[product_id]
    # minimum_price_storage = min(product_storages, key=lambda storage: (min(storages[storage][product_id]), storage))
    minimum_price_storage = min((storages[storage][product_id], storage) for storage in product_storages)
    return f"{minimum_price_storage[1]} {minimum_price_storage[0] + price}"


if __name__ == '__main__':
    num_storages = int(input())
    for _ in range(num_storages):
        storage_info = tuple(map(int, input().split()))
        storage_products = {}
        for product_id, price in list(zip(storage_info[2::2], storage_info[3::2])):
            storage_products[product_id] = min(storage_products.get(product_id, 2e10), price)
            products[product_id].append(storage_info[0])
        storages[storage_info[0]] = storage_products
    num_requests = int(input())
    for _ in range(num_requests):
        product_id, price = tuple(map(int, input().split()))
        result.append(find_lowest_price(product_id, price))
    for row in result:
        print(row)
