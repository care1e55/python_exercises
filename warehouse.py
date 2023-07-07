
def max_sell_price(prices, current_max_index, exit_index, current_max):
    total_prices = [price * i for i, price in enumerate(prices, start=1)]
    new_max = max(total_prices)
    if new_max < 0:
        return current_max
    new_max_index = total_prices.index(new_max)
    current_max_index += new_max_index
    current_max += new_max
    print(prices)
    print(total_prices)
    print(new_max_index, current_max_index,  exit_index)
    if current_max_index != exit_index:
        current_max = max_sell_price(prices[new_max_index+1:], current_max_index+1, exit_index, current_max)
    return current_max


if __name__ == '__main__':
    n = int(input())
    prices = [int(i) for i in input().split()]
    # print(prices)
    answer = max_sell_price(prices, 0, n-1, 0)
    print(answer)
