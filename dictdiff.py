from typing import Dict, Any, List

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}

def dictdiff(d1:Dict, d2:Dict) -> Dict[str, List[int]]:
    result = {}
    for key in d1.keys() | d2.keys():
        if key not in d1 or key not in d2:
            result[key] = [d1.get(key), d2.get(key)]
    return result

print(dictdiff(d1, d1))
print(dictdiff(d1, d2))
print(dictdiff(d3, d4))
print(dictdiff(d1, d5))
