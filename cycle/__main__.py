import pygame
from pygame.locals import *
from pygame import mixer
import sys
import constants
from director import Director
from trail import Trail
from handle_collision_action import HandleCollisionsAction
from video_services import VideoServices

# Initialize pygame
pygame.init()
#width = 800
#height = 800
#window = pygame.display.set_mode((width,height))
#bg_img = pygame.image.load('byui-blackbox.jpg')
#bg_img = pygame.transform.scale(bg_img,(width,height))
 
mixer.init()
mixer.music.load('cycle/audio/bensound-summer_mp3_music.wav')
mixer.music.play()
 
#runing = True
#while runing:
#    window.blit(bg_img,(0,0))
#    for event in pygame.event.get():
#        if event.type == QUIT:
#
#            runing = False
#    pygame.display.update()
#pygame.quit()

def main():
    video_services = VideoServices()
    director = Director()

if __name__ == "__main__":
    main()