import re
if __name__ == '__main__':
    print(re.sub(r'^(.*?)$', r'<a href="tel:\1">\1</a>', input()))
