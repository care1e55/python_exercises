
def joinnumbers(range_to: int):
    return ",".join(str(number) for number in range(range_to) if number < 10)

if __name__=="__main__":
    print(joinnumbers(15))
