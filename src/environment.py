import numpy as np
import random

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.generate_grid()

    def generate_grid(self):
        grid = np.zeros((self.width, self.height))
        
        for i in range(self.width):
            for j in range(self.height):
                if random.random() < 0.2:
                    grid[i][j] = 1  # obstacle

        return grid