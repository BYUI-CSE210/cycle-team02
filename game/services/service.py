import pygame
from pygame.locals import *
import constants
from game.casting.trail import Trail
from game.scripting.handle_collision_action import HandleCollisionsAction



class Service:
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
        self.collision = HandleCollisionsAction() 
        
        self.x1 = 1
        self.y1 = 0
        self.x2 = -1
        self.y2 = 0