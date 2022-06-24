from pygame.locals import *
from game.services.keyboard_service import KeyBoardService



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
        
        KeyBoardService()
        
        