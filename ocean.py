import sys
import csv
import requests
from collections import defaultdict

result = defaultdict(list)

if __name__ == "__main__":
    host, port = sys.argv[1], sys.argv[2]
    jtext = requests.get(f'http://{host}:{port}').json()

    for i in jtext:
        for key, value in i.items():
            result[key] += value

    to_tsv = defaultdict(list)
    for key, values in result.items():
        to_tsv[key].append(max(values))
        to_tsv[key].append(min(values))
        to_tsv[key].append(round(sum(values) / len(values), 2))
        to_tsv[key].append(sum(values))

    with open('truth.csv', 'w', newline='') as csvfile:
        for key in key in sorted(to_tsv.keys(), key=lambda x: x.lower()):
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow([key] + to_tsv[key])
