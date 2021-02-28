from typing import Tuple
from copy import copy


class Robot():

    moves = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0),
    }

    limits = (-1, 101)

    def __init__(self, current_pos: Tuple[int, int] = (0, 0)):
        self.current_pos = current_pos
        self.result_path = [current_pos]

    def _in_limits(self, pos: Tuple[int, int]):
        if self.limits[0] < pos[0] < self.limits[1] and \
                self.limits[0] < pos[1] < self.limits[1]:
            return True
        return False 

    def move(self, path: str) -> Tuple[int, int]:
        for move in path:
            new_pos = \
                self.current_pos[0] + self.moves[move][0], \
                self.current_pos[1] + self.moves[move][1]
            if self._in_limits(new_pos):
                self.current_pos = new_pos
            self.result_path.append(copy(self.current_pos))
        return self.current_pos

    def path(self) -> Tuple[Tuple[int, int]]:
        return tuple(self.result_path)
