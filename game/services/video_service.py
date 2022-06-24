import pygame
from pygame.locals import *
import constants
from game.casting.trail import Trail
from game.services.keyboard_service import KeyBoardService
from game.services.service import Service




class VideoService(Service):
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        super().__init__()

        self._debug = debug    
        
        self._cycle1 = Trail(1, constants.green, constants.red, 0)
        self._cycle2 = Trail(2, constants.seablue , constants.red, constants.width)


       
        
        loop = True
        while loop:
            key = KeyBoardService()
            key.key_input()     
                
            constants.display.fill(constants.background)
            self.collision.drawGrid()
            self._cycle1.draw()
            self._cycle2.draw()

            self._cycle1.move(self.x1, self.y1)
            self._cycle2.move(self.x2, self.y2)

            self._cycle1.checkIfHit(self._cycle2)
            self._cycle2.checkIfHit(self._cycle1)
            
            pygame.display.update()
            constants.clock.tick(10)


       
    