from abc import ABC, abstractmethod


class BaseProgression(ABC):

    @abstractmethod
    def add(self):
        pass


class Progression(BaseProgression):
    def __init__(self, start: int, stop: int):
        self.prev = start - 1
        self.stop = stop

    def add(self):
        self.prev += 1

    def __next__(self):
        self.add()
        if self.prev >= self.stop:
            raise StopIteration()
        return self.prev

    def __iter__(self):
        return self


class ArithmeticProgression(Progression):
    def __init__(self, start: int, stop: int, increment: int):
        self.prev = start - increment
        self.increment = increment
        self.stop = stop

    def add(self):
        self.prev += self.increment


class GeometricProgression(Progression):
    def __init__(self, start: int, stop: int, multiplier: int):
        self.prev = start // multiplier
        self.multiplier = multiplier
        self.stop = stop

    def add(self):
        self.prev *= self.multiplier


class FibonacciProgression(Progression):
    def __init__(self, first: int, second: int, stop: int):
        self.prev = second - first
        self.current = first
        self.stop = stop

    def add(self):
        self.prev, self.current = self.current, self.current + self.prev
