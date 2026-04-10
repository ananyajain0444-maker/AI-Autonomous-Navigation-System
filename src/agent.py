class Agent:
    def __init__(self, start):
        self.position = start

    def move(self, new_position):
        self.position = new_position