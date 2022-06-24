import pygame
from pygame.locals import *
from game.casting.trail import Trail
from game.scripting.handle_collision_action import HandleCollisionsAction
from game.services.service import Service



class KeyBoardService(Service):
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
        super().__init__()
        
       
        
    def key_input(self):  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.collision.close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.collision.close()
                if event.key == pygame.K_UP:
                    if not (self.x2 == 0 and self.y2 == 1):
                        self.x2 = 0
                        self.y2 = -1
                if event.key == pygame.K_DOWN:
                    if not (self.x2 == 0 and self.y2 == -1):
                        self.x2 = 0
                        self.y2 = 1
                if event.key == pygame.K_LEFT:
                    if not (self.x2 == 1 and self.y2 == 0):
                        self.x2 = -1
                        self.y2 = 0
                if event.key == pygame.K_RIGHT:
                    if not (self.x2 == -1 and self.y2 == 0):
                        self.x2 = 1
                        self.y2 = 0
                if event.key == pygame.K_w:
                    if not (self.x1 == 0 and self.y1 == 1):
                        self.x1 = 0
                        self.y1 = -1
                if event.key == pygame.K_s:
                    if not (self.x1 == 0 and self.y1 == -1):
                        self.x1 = 0
                        self.y1 = 1
                if event.key == pygame.K_a:
                    if not (self.x1 == 1 and self.y1 == 0):
                        self.x1 = -1
                        self.y1 = 0
                if event.key == pygame.K_d:
                    if not (self.x1 == -1 and self.y1 == 0):
                        self.x1 = 1
                        self.y1 = 0
                
            
        
       
        
        