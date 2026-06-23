import pygame

from Code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Code.Level import Level
from Code.Menu import Menu


#Classe Game
class Game:
    #Construtor da Classe Game
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))

    def run(self,):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()


            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, "Level1")
                level_return = level.run()
            elif menu_return == MENU_OPTION[1]:
                pass
            elif menu_return == MENU_OPTION[2]:
                pass
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()
            else:
                pass


