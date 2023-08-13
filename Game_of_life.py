from random import randint
from copy import deepcopy


class SingletonsMeta(type):
    instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instance:
            cls.instance[cls] = super(SingletonsMeta, cls).__call__(*args, **kwargs)
        return cls.instance[cls]


class GameOfLife(metaclass=SingletonsMeta):
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.generation_count = 0
        self.world = self.__generate_field()

    @staticmethod
    def __get_neighbours(world, position, system=None):
        if system is None:
            system = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        neighbour_count = 0
        for item in system:
            if world[(position[0] + item[0]) % len(world)][(position[1] + item[1]) % len(world[0])] == 1:
                neighbour_count += 1
        return neighbour_count

    def get_new_generation(self):
        new_world = deepcopy(self.world)
        for row in range(self.height):
            for col in range(self.width):
                neighbours = self.__get_neighbours(self.world, (row, col))
                if self.world[row][col] == 1:
                    if neighbours > 3 or neighbours < 2:
                        new_world[row][col] = 0
                else:
                    if neighbours == 3:
                        new_world[row][col] = 1
        self.world = deepcopy(new_world)
        self.generation_count += 1

    def __generate_field(self):
        return [[randint(0, 1) for _ in range(self.width)] for _ in range(self.height)]
