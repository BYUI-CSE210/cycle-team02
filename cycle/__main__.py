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

#Initialize music mixer
mixer.init()
#mixer.music.load('bensound-summer_ogg_music.wav')
#mixer.music.play()


def main():
    video_services = VideoServices()
    director = Director()





if __name__ == "__main__":
    main()