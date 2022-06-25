import pygame
from pygame.locals import *
import constants
from game.casting.trail import Trail
from game.services.video_service import VideoService



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
        self._loop = True
    
        self._cycle1 = Trail(1, constants.green, constants.red, 0)
        self._cycle2 = Trail(2, constants.seablue , constants.red, constants.width)

        self.x1 = 1
        self.y1 = 0
        self.x2 = -1
        self.y2 = 0

        self.video = VideoService()

    def start_game(self): 
        while self._loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.video.close_window()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.video.close_window()
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
                    
                
            constants.display.fill(constants.background)

            self.video.draw_board()

            self._cycle1.draw_trail()
            self._cycle2.draw_trail()

            self._cycle1.move_cycle(self.x1, self.y1)
            self._cycle2.move_cycle(self.x2, self.y2)

            self._cycle1.check_collision(self._cycle2)
            self._cycle2.check_collision(self._cycle1)
            
            pygame.display.update()
            constants.clock.tick(10)
