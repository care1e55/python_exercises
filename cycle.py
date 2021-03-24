
class Circle():
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number

    def __iter__(self):
        return CircleIterator(self.sequence, self.number)


class CircleIterator:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __next__(self):
        self.index +=1
        if self.index >= self.number:
            raise StopIteration
        return self.sequence[self.index%len(self.sequence)]


if __name__ == '__main__':
    c = Circle('abc', 5)
    print(list(c))

