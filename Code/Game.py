import pygame

from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Menu import Menu


#Classe Game
class Game:
    #Construtor da Classe Game
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))

    def run(self,):
        pygame.mixer.music.load("./Asset/MusicaMenu.mp3")
        pygame.mixer.music.play(-1)

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check por todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting...")
                    pygame.quit() # Close Window
                    quit() # Fecha o pygame