import random
#0 = nothing, 1 = tile, 2 = enemy

class Level():
    def __init__(self):
        #the screen is 12 tiles high, 16 tiles wide
        self.screenMap = [
            [0] * 17,
            [0] * 17,
            [0] * 17,
            [0] * 17,
            [0] * 17,
            [0] * 17,
            [0] * 17,
            [0] * 17,
            [0] * 17,
            [0] * 17,
            [0] * 17,
            [1] * 17
        ]
        self.HEIGHT = 12
        self.WIDTH = 16
    def gen_column(self):
        for i in range(len(self.screenMap)):
            if self.screenMap[i][15]:
                print("i = ", i)
                x = random.randint(i - 2, self.HEIGHT - 1)
                print("x = ", x)
                self.screenMap[x][16] = 1
                         