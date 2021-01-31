from collections import Counter

words = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_common_letter_count(word: str) -> int:
    return Counter(word).most_common(1)[0][1]


if __name__ == '__main__':
    print(max(words, key=most_common_letter_count))
    print(max(words, key=lambda word: Counter(word).most_common(1)[0][1]))
    print(sorted(words, key=most_common_letter_count)[-1])
