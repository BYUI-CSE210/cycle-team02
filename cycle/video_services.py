import pygame
from pygame.locals import *
from pygame import mixer
import sys
import constants
from trail import Trail
from handle_collision_action import HandleCollisionsAction




class VideoServices:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug

       
    