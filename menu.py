import re


def prerify_number(number: str) -> str:
    large_num = reversed(number)
    result = [
        digit if pos % 3 else " " + digit
        for pos, digit in enumerate(large_num, 1)
    ]
    return "".join(reversed(result)).strip() + "р"


if __name__ == '__main__':
    with open("input.txt") as file:
        for line in file.readlines():
            price_dollar = re.findall(f'\\$([0-9]+)', line)
            if price_dollar:
                ruble_price = int(price_dollar[0])*75
                print(
                    re.sub(
                        f'\\$([0-9]+)',
                        prerify_number(str(ruble_price)), line),
                    end=''
                )
            else:
                print(line, end='')
