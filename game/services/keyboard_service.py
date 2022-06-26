import pygame
from pygame.locals import *
import constants
from game.services.video_service import VideoService
from game.casting.trail import Trail

pygame.init()

class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self.x1 = 1
        self.y1 = 0
        self.x2 = -1
        self.y2 = 0

        self._cycle1 = Trail(1, constants.green, constants.red, 0)
        self._cycle2 = Trail(2, constants.seablue , constants.red, constants.width)

        self.video = VideoService()

    
    def is_key_down(self):
        self._loop = True

        while self._loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.video.close_window()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.video.close_window()
                    elif event.key == pygame.K_r:
                        #self.director.start_game()                                                              
                        self.is_key_down
                    elif event.key == pygame.K_UP:
                        if not (self.x2 == 0 and self.y2 == 1):
                            self.x2 = 0
                            self.y2 = -1
                    elif event.key == pygame.K_DOWN:
                        if not (self.x2 == 0 and self.y2 == -1):
                            self.x2 = 0
                            self.y2 = 1
                    elif event.key == pygame.K_LEFT:
                        if not (self.x2 == 1 and self.y2 == 0):
                            self.x2 = -1
                            self.y2 = 0
                    elif event.key == pygame.K_RIGHT:
                        if not (self.x2 == -1 and self.y2 == 0):
                            self.x2 = 1
                            self.y2 = 0
                    elif event.key == pygame.K_w:
                        if not (self.x1 == 0 and self.y1 == 1):
                            self.x1 = 0
                            self.y1 = -1
                    elif event.key == pygame.K_s:
                        if not (self.x1 == 0 and self.y1 == -1):
                            self.x1 = 0
                            self.y1 = 1
                    elif event.key == pygame.K_a:
                        if not (self.x1 == 1 and self.y1 == 0):
                            self.x1 = -1
                            self.y1 = 0
                    elif event.key == pygame.K_d:
                        if not (self.x1 == -1 and self.y1 == 0):
                            self.x1 = 1
                            self.y1 = 0
                    elif event.key == pygame.K_p:
                        self._is_paused()

                    

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


    def _is_paused(self):
        
        self.paused = True
        
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.paused = False
                        self.is_key_down()
                        
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    
            #constants.display.fill(constants.background)
            
            text = constants.font.render("Paused", True, constants.red)
            pygame.display.update()
            constants.clock.tick(10)

        
          