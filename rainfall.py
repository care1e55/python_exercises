from collections import defaultdict

def rainfall():
    report = defaultdict(int)
    while True:
        try:
            city = input().strip()
            if not city:
                break
            rainfalls = int(input().strip())
            report[city] += rainfalls
        except:
            continue
    return report

if __name__ == '__main__':
    print(rainfall())
