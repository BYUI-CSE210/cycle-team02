
import pygame
import constants
from game.scripting.handle_collision_action import HandleCollisionsAction
from game.casting.actor import Actor



pygame.init()

# Trail Class
class Trail(Actor):
    def __init__(self, number, trail_color, head_color, side):
        super().__init__(side)
        
        self.speed = 10
        self.trail = trail_color
        self.head = head_color
        self.history = [[self.x, self.y]]
        self.number = number
        self.length = 1

    # Draw / Show the Bike
    def draw_trail(self):
        for i in range(len(self.history)):
            if i == self.length - 1:
                pygame.draw.rect(constants.display, self.head, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:    
                pygame.draw.rect(constants.display, self.trail, (self.history[i][0], self.history[i][1], self.w, self.h))

    # Move the Bike
    def move_cycle(self, xdir, ydir):
        self.x += xdir*self.speed
        self.y += ydir*self.speed
        self.history.append([self.x, self.y])
        self.length += 1
        if self.x < 0 or self.x > constants.width or self.y < 0 or self.y > constants.height:
            self.collision.execute(self.number)

    # Check if Cycle Collides with Route
    def check_collision(self, opponent):

        self.collision = HandleCollisionsAction()

        if abs(opponent.history[opponent.length - 1][0] - self.history[self.length - 1][0]) < self.w and abs(opponent.history[opponent.length - 1][1] - self.history[self.length - 1][1]) < self.h:
            self.collision.execute(0)
        for i in range(opponent.length):
            if abs(opponent.history[i][0] - self.history[self.length - 1][0]) < self.w and abs(opponent.history[i][1] - self.history[self.length - 1][1]) < self.h:
                self.collision.execute(self.number)

        for i in range(len(self.history) - 1):
            if abs(self.history[i][0] - self.x) < self.w and abs(self.history[i][1] - self.y) < self.h and self.length > 2:
                self.collision.execute(self.number)

