
import pygame
import constants
from game.services.video_service import VideoService



pygame.init()

class HandleCollisionsAction:
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the trails collide, or one trail collides with its segments, 
    or the game is over.

    
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        #self._is_end_game = False

        self.video = VideoService()

    def execute(self, number):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.video.close_window()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.video.close_window()
                    if event.key == pygame.K_r:
                        #main()
                        pass
            if number == 0:
                text = constants.font.render("Oops! What a double collision!", True, constants.white)
            else:
                text = constants.font.render("Player %d lost!" %(number), True, constants.white)

            constants.display.blit(text, (50, constants.height/2))
            
            pygame.display.update()
            constants.clock.tick(60)


