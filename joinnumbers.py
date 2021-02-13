from typing import List, Any, Dict
import string 

def joinnumbers(range_to: int) -> str:
    return ",".join(str(number) for number in range(range_to) if number < 10)

def add_numbers(in_string: str) -> float:
    return sum(
        float(i) for i in in_string.split() if i.isdigit()
    )

def flatten(inlist: List[List[Any]]):
    return [j for i in inlist for j in i]

def flip_dict(in_dict: Dict[str, int]) -> Dict[int, str]:
    return {value:key for key, value in in_dict.items()}

if __name__=="__main__":
    print(joinnumbers(15))
    print(add_numbers("10 abc 20 de44 30 55fg 40"))
    print(flatten([[1,2], [3,4]]))
    print(flip_dict({'a':1, 'b':2, 'c':3}))
    print({ key: value for value, key in enumerate(string.ascii_lowercase, 1)})
