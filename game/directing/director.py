import pygame
from pygame.locals import *
import constants
from game.casting.trail import Trail
from game.scripting.handle_collision_action import HandleCollisionsAction



class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        #self._video_service = video_service
        loop = True
    
        cycle1 = Trail(1, constants.green, constants.red, 0)
        cycle2 = Trail(2, constants.seablue , constants.red, constants.width)

        x1 = 1
        y1 = 0
        x2 = -1
        y2 = 0

        collision = HandleCollisionsAction()
        
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    collision.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        collision.close()
                    if event.key == pygame.K_UP:
                        if not (x2 == 0 and y2 == 1):
                            x2 = 0
                            y2 = -1
                    if event.key == pygame.K_DOWN:
                        if not (x2 == 0 and y2 == -1):
                            x2 = 0
                            y2 = 1
                    if event.key == pygame.K_LEFT:
                        if not (x2 == 1 and y2 == 0):
                            x2 = -1
                            y2 = 0
                    if event.key == pygame.K_RIGHT:
                        if not (x2 == -1 and y2 == 0):
                            x2 = 1
                            y2 = 0
                    if event.key == pygame.K_w:
                        if not (x1 == 0 and y1 == 1):
                            x1 = 0
                            y1 = -1
                    if event.key == pygame.K_s:
                        if not (x1 == 0 and y1 == -1):
                            x1 = 0
                            y1 = 1
                    if event.key == pygame.K_a:
                        if not (x1 == 1 and y1 == 0):
                            x1 = -1
                            y1 = 0
                    if event.key == pygame.K_d:
                        if not (x1 == -1 and y1 == 0):
                            x1 = 1
                            y1 = 0
                    
                
            constants.display.fill(constants.background)
            collision.execute()
            cycle1.draw()
            cycle2.draw()

            cycle1.move(x1, y1)
            cycle2.move(x2, y2)

            cycle1.checkIfHit(cycle2)
            cycle2.checkIfHit(cycle1)
            
            pygame.display.update()
            constants.clock.tick(10)
