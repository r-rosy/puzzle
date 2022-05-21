from enum import Enum


class GameStatus(Enum):
    readied = 1,
    started = 2,
    over = 3,
    win = 4,
