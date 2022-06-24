import pygame

pygame.init()

# Constants
# =====================================================================
width = 1200
height = 800
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cycle Game")
clock = pygame.time.Clock()

# Colors
background = (0, 0, 0)
white = (236, 240, 241)
yellow = (241, 196, 15)
darkYellow = (247, 220, 111)
red = (231, 76, 60)
darkRed = (241, 148, 138)
darkBlue = (40, 116, 166)
green = (0, 255, 0)
seablue = (0, 220, 255)
lightpink = (255, 100, 255)

font = pygame.font.SysFont("Helvetica", 40)

w = 10
# =====================================================================
#End Constants