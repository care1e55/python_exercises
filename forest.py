import re

if __name__ == '__main__':
    while True:
        try:
            print(re.sub(r'"(.*?)"', r'«\1»', input()))
        except EOFError:
            break
