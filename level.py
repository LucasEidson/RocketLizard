#0 = nothing, 1 = tile, 2 = enemy
level1 = [
    [0] * 100,
    [0] * 100,
    [0] * 100,
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 1, 2],
    [1]* 100,
]
class Level():
    def __init__(self):
        pass
    #eventually I will need to generate a semi-random map for the level!