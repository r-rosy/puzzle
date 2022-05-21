import random
from enum import Enum
from Source.setting import Settings
from Source.component.Mine import Mine
from Source.component.BlockStaus import BlockStaus

setting = Settings()


class MineBlock:
    def __init__(self):
        self.opportunity = 3
        self._block = [[Mine(i, j) for i in range(3) for j in range(3)]]
        # 设置标记点
        for i in random.sample(range(3 * 3), 5):
            self._block[i // 3][i % 3].value = 1

    def get_block(self):
        return self._block

    block = property(fget=get_block)

    def getmine(self, x, y):
        return self._block[y][x]

    def open_mine(self, x, y, opportunity):
        # 猜错了
        self.opportunity = opportunity
        if not self._block[y][x].value:
            self._block[y][x].status = BlockStaus.empty
            opportunity -= 1

            if opportunity < 0:
                return False
            return True
        # 猜对了
        if self._block[y][x].value:
            self._block[y][x].status = BlockStaus.opened
            return True
        return True
