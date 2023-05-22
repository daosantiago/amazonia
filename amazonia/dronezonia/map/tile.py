import random

from .colors import MyColors


class Tile:

    def __init__(self, id, row, col):
        self.id = id
        self.row = row
        self.col = col
        self.color = MyColors.empty()
        self.value = 0
        self.neighbors = []
        self.dist = float('inf')
        self.visited = False
        self.previous = None
        self.cost = round(random.uniform(10.00, 30.00), 2)
        self.coming_from = None

    @classmethod
    def get_next_id(cls):
        cls.id_counter += 1
        return cls.id_counter

    def init_cost(self):
        """Init tile's cost in costs matrix. Theres no cost for self tile"""
        if self.row == self.col:
            self.dist = 0
        else:
            self.dist = float('inf')

    def __lt__(self, other):
        """It's needed to compare priority in heapq"""
        return self.dist < other.dist

    def __str__(self) -> str:
        """Returns the tile as string chess coordinates format"""
        letter = chr(self.row + 65)  # 65 é o código Unicode para a letra 'A'
        return f"{letter}{self.col+1}"

    def as_dict(self):
        tile_dict = {}
        tile_dict['id'] = self.id
        tile_dict['row'] = self.row
        tile_dict['col'] = self.col
        return tile_dict
