from math import ceil

MASK_ONE_PRICE = 0.55
MASK_PACK_24_PRICE = 11
MASK_PACK_24_16_PRICE = 160

MASK_24_COUNT = 24
MASK_24_16_COUNT = 24*16

MASK_ONE_24_PRICE = 11 / MASK_24_COUNT
MASK_ONE_24_16_PRICE = 160 / MASK_24_16_COUNT


def mask_price(count):

    price_24_16_count = ceil(count / MASK_24_16_COUNT)
    price_24_16_truediv_count = count // MASK_24_16_COUNT
    price_24_16_left_count = count - price_24_16_truediv_count*MASK_24_16_COUNT
    price_24_16_price = price_24_16_count * MASK_PACK_24_16_PRICE
    price_24_16_truediv_price = price_24_16_truediv_count * MASK_PACK_24_16_PRICE

    price_24_count = ceil(price_24_16_left_count / MASK_24_COUNT)
    price_24_truediv_count = price_24_16_left_count // MASK_24_COUNT
    price_24_left_count = count - price_24_truediv_count*MASK_24_COUNT - price_24_16_truediv_count*MASK_24_16_COUNT
    price_24_price = price_24_count * MASK_PACK_24_PRICE
    price_24_truediv_price = price_24_truediv_count * MASK_PACK_24_PRICE

    price_one_left = price_24_left_count * MASK_ONE_PRICE
    last_price = price_one_left + price_24_truediv_price

    prices = (
        price_24_16_price,
        price_24_price + price_24_16_truediv_price,
        last_price
    )

    min_price_arg = 0
    min_price = prices[min_price_arg]
    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
            min_price_arg = i

    solutions = (
        (price_24_16_count, 0, 0)[::-1],
        (price_24_16_truediv_count, price_24_count, 0)[::-1],
        (price_24_16_truediv_count, price_24_truediv_count, price_24_left_count)[::-1]
    )

    print(*solutions[min_price_arg])


if __name__ == '__main__':
    mask_price(int(input()))