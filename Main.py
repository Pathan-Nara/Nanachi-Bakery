import pygame
from components.constants import SCREEN 
pygame.init()
from menus.MainMenu import MainMenu

def main():
    menu = MainMenu(SCREEN)
    menu.run()



if __name__ == "__main__":
    main()