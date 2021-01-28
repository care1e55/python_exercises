from typing import List

def mysum(*args) -> int:
    result = 0
    for i in args:
        result += i
    return result

def mysum2(args: List[int], additional: int = 0) -> int:
    result = additional
    for i in args:
        result += i
    return result

def mymean(args: List[int]) -> int:
    result = 0
    for i in args:
        result += i
    return result/len(args)


if __name__=="__main__":
    # result = mysum1(1,2,3)
    # result = mysum2([1,2,3], 5)
    result = mymean([1,2,3])
    print(result)
