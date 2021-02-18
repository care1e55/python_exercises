root = "комментар"

endings = {
    "0": "иев",
    "1": "ий",
    "2": "ия",
    "3": "ия",
    "4": "ия",
    "5": "иев",
    "6": "иев",
    "7": "иев",
    "8": "иев",
    "9": "иев",
}

if __name__ == '__main__':
    input_string = input()
    if 9 < int(input_string) < 21:
        result = root + endings["0"]
    else:
        result = root + endings[input_string[-1]]
    print(result)
