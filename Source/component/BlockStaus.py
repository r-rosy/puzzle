import random
from enum import Enum


class BlockStaus(Enum):
    normal = 1  # 未点击
    opened = 2  # 已点击
    mine = 3  # 标记图案
    empty = 4  # 无标记
