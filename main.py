import random
class Character:
    def __init__(self, x, y, speed):
        self.center_x = x
        self.center_y = y
        self.speed = speed
        self.change_x = 0
        self.change_y = 0



class Player(Character):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.score = 0
        self.lives = 3
    def move(self):
        self.center_x = self.change_x * self.speed
        self.center_y = self.change_y * self.speed


class Enemy(Character):
    def __init__(self,x,y ,speed):
        super().__init__(x, y, speed)
        self.time_to_change_direction = 0
    def pick_new_direction(self):
        moves = [(1,0), (-1,0), (0,1), (0,-1), (0,0)]
        move = random.choice(moves)
        self.change_x = move[0]
        self.change_y = move[1]
        self.time_to_change_direction = random.uniform(0.3,1.0)
    def update(self):
        while self.time_to_change_direction != 0:
            self.time_to_change_direction -= 1/60
        self.pick_new_direction()

class Wall:
    def __init__(self,x, y):
        self.center_x = x
        self.center_y = y

