
import pygame
import sys
import constants



pygame.init()

class HandleCollisionsAction:
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the trail collides
    with the food, or the trail collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        #self._is_game_over = False

    def gameOver(self, number):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_window()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.close_window()
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

    def drawGrid(self):
        squares = 100 
        for i in range(int(constants.width/squares)):
            pygame.draw.line(constants.display, constants.lightpink, (i*squares, 0), (i*squares, constants.height))
            pygame.draw.line(constants.display, constants.lightpink, (0, i*squares), (constants.width, i*squares))

    def close_window(self):
        pygame.quit()
        sys.exit()

