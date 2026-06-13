class Weapon:

    def __init__(self):

        self.level = 1
        self.type = 0  # 0: pistol, 1: shotgun, 2: machinegun

    def upgrade(self):

        self.level += 1

        if self.level % 3 == 0:
            self.type = (self.type + 1) % 3
