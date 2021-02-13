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

def gen_gematria_dict():
    return { 
        key: value for value, key in enumerate(string.ascii_lowercase, 1)
    }

def gematria_for(word: str, gematria_dict):
    return sum(
        gematria_dict[letter] for letter in word
    )

def gematria_equal_words(word: str, gematria_dict):
    score = gematria_for(word, gematria_dict)
    lenght = len(word)
    subset_sum([i for i in range(1,score)], score)
    
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    if s == target:
        print("".join([inverse_gematria_dict[i] for i in partial]))
    if s > target:
        return None
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])
        # subset_sum(numbers, target, partial + [n])



if __name__=="__main__":
    print(joinnumbers(15))
    print(add_numbers("10 abc 20 de44 30 55fg 40"))
    print(flatten([[1,2], [3,4]]))
    print(flip_dict({'a':1, 'b':2, 'c':3}))
    gematria_dict = gen_gematria_dict()
    inverse_gematria_dict = {v:k for k,v in gematria_dict.items()}
    print(gematria_for("cat", gematria_dict))
    gematria_equal_words("cat", gematria_dict)
