import re
from collections import Counter

if __name__ == '__main__':
    result = Counter()
    with open("input.txt") as file:
        for line in file.readlines():
            line = re.sub('[\\s\\d]', '', line)
            result += Counter(line)
    print(*[v for k, v in sorted(result.most_common(4), key=lambda x: x[0])])
