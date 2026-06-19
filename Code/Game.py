import pygame

from Code.Menu import Menu


#Classe Game
class Game:
    #Construtor da Classe Game
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (600, 480))

    def run(self,):
        while True:
            menu = Menu(self.window)
            pass
            menu.run()
            # Check por todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting...")
                    pygame.quit() # Close Window
                    quit() # Fecha o pygame