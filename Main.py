import pygame
from constants import SCREEN 
pygame.init()
from MainMenu import MainMenu

def main():
    menu = MainMenu(SCREEN)
    menu.run()



if __name__ == "__main__":
    main()