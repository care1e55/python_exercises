# Напишите класс Robot, который инициализируется с начальными координатами
# – положением Робота на плоскости, обе координаты заключены в пределах от 0 до 100.
#
# Робот может передвигаться на одну клетку вверх (N), вниз (S), вправо (E), влево (W).
# Выйти за границы плоскости Робот не может.
#
# Метод move() принимает строку – последовательность команд перемещения робота,
# каждая буква строки соответствует перемещению на единичный интервал в направлении,
# указанном буквой. Метод возвращает кортеж координат – конечное положение Робота после перемещения.
#
# Метод path() вызывается без аргументов и возвращает список кортежей координат точек,
# по которым перемещался Робот при последнем вызове метода move.
# Если метод не вызывался, возвращает список с одним кортежем – начальным положением Робота.


from typing import Tuple
from copy import copy

MOVES = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
}

LIMITS = (-1, 101)


class Robot:

    def __init__(self, current_pos: Tuple[int, int] = (0, 0)):
        self.result_path = [current_pos]

    @property
    def current_pos(self):
        return self.result_path[-1]

    @staticmethod
    def _in_limits(pos: Tuple[int, int]):
        if LIMITS[0] < pos[0] < LIMITS[1] and \
                LIMITS[0] < pos[1] < LIMITS[1]:
            return True
        return False

    def _new_pos(self, move):
        return (
            self.current_pos[0] + MOVES[move][0],
            self.current_pos[1] + MOVES[move][1]
        )

    def move(self, path: str) -> Tuple[int, int]:
        for move in path:
            new_pos = self._new_pos(move)
            if Robot._in_limits(new_pos):
                self.result_path.append(new_pos)
        return self.current_pos

    def path(self) -> Tuple[Tuple[int, int]]:
        return tuple(self.result_path)
