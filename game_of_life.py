from random import randint
from copy import deepcopy


class SingletonsMeta(type):
    instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instance:
            cls.instance[cls] = super(SingletonsMeta, cls).__call__(*args, **kwargs)
        return cls.instance[cls]


class GameOfLife(metaclass=SingletonsMeta):
    def __init__(self):
        self.width = 20
        self.height = 20
        self.generation_count = 0
        self.world = self.__generate_field()
        self.old_world = deepcopy(self.world)

    def __generate_field(self):
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    def __get_neighbours(self, position, system=None):
        if system is None:
            system = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        neighbour_count = 0
        for item in system:
            if self.world[(position[0] + item[0]) % self.width][(position[1] + item[1]) % self.height] == 1:
                neighbour_count += 1
        return neighbour_count

    def populate_world(self):
        for row in range(self.height):
            for col in range(self.height):
                self.world[row][col] = randint(0, 1)

    def get_new_world(self, width=20, height=20):
        self.width = width
        self.height = height
        self.world = self.__generate_field()
        self.generation_count = 0

    def get_new_generation(self):
        self.old_world = deepcopy(self.world)
        new_world = self.__generate_field()
        for row in range(self.height):
            for col in range(self.width):
                neighbours = self.__get_neighbours((row, col))
                if self.world[row][col] == 1:
                    if neighbours > 3 or neighbours < 2:
                        new_world[row][col] = 0
                else:
                    if neighbours == 3:
                        new_world[row][col] = 1
        self.world = deepcopy(new_world)
        self.generation_count += 1



