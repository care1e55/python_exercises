def is_odd(number: int) -> bool:
    return bool(number % 2)


# def closest_palindrome(word: str) -> str:
#     center = len(word) // 2
#     left = word[:center]
#     if is_odd(len(word)):
#         palindrome = left + word[center] + left[::-1]
#     else:
#         palindrome = left + left[::-1]
#     return "".join(palindrome)


def closest_palindrome(number):
    while True:
        number+=1
        if str(number) == str(number)[::-1]:
            return number


def palindrome_distance():
    number = input()
    anagram = closest_palindrome(int(number))
    print(int(anagram) - int(number))


if __name__ == '__main__':
    palindrome_distance()