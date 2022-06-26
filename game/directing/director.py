import pygame
from pygame.locals import *
import constants
from game.casting.trail import Trail
from game.services.video_service import VideoService
from game.services.keyboard_service import KeyboardService



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
         
        self.key = KeyboardService()

    def start_game(self): 
        self.key.is_key_down()                  
                
            
