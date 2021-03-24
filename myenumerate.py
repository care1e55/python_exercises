
class MyEnumerate():

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.index, self.iterator.__next__()


def myenumerate(iterable):
    index = 0 
    for i in iterable:
        yield index, i
    index +=1


if __name__ == '__main__':
    for i in MyEnumerate(range(10)):
        print(i)

    for i in myenumerate(range(10)):
        print(i)

