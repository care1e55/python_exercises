import json

result = []

if __name__ == '__main__':
    n = int(input())
    test_json = json.loads("".join(input() for _ in range(n)))
    for element in test_json:
        result.append(element['data']['key'])
    print(len(set(result)))
