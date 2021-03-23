
class MyEnumerate():

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.index, self.iterator.__next__()


if __name__ == '__main__':
    for i in MyEnumerate(range(10)):
        print(i)
