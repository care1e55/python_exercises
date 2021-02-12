from typing import List

vowels = {'a', 'e', 'i', 'o', 'u'}

def check_vocalic(word: str):
    return all([letter in vowels for letter in word])

if __name__ == "__main__":
    with open('words.txt', mode='r') as file:
        result = set(
            filter(
                check_vocalic, map(str.strip, file.readlines())
            )
        )
    print(result)
