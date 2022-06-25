
import pygame
import sys
import constants
from pygame.locals import *




class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug
    
    def draw_board(self):
        squares = 100 
        for i in range(int(constants.width/squares)):
            pygame.draw.line(constants.display, constants.lightpink, (i*squares, 0), (i*squares, constants.height))
            pygame.draw.line(constants.display, constants.lightpink, (0, i*squares), (constants.width, i*squares))

    def close_window(self):
        pygame.quit()
        sys.exit()

       
    