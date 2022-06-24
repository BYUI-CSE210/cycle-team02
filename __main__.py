import pygame
from pygame.locals import *
from pygame import mixer
from game.directing.director import Director
from game.services.video_service import VideoService



 # Initialize pygame
pygame.init()

#Initialize music mixer
mixer.init()
#mixer.music.load('bensound-summer_ogg_music.wav')
#mixer.music.play()


def main():
    video_service = VideoService()
    director = Director()





if __name__ == "__main__":
    main()