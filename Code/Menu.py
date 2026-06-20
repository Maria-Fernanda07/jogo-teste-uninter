import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.Const import WIN_WIDTH, COR_AZUL, MENU_OPTION, COR_VERDE


#Classe Menu
class Menu:

    def __init__(self, window):
        #Imagem de fundo do menu
        self.window = window
        self.surf = pygame.image.load("./Asset/FundoPraiaMenu.png")
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def run(self,):
        #Musica do menu
        pygame.mixer.music.load("./Asset/MusicaMenu.mp3")
        pygame.mixer.music.play(-1)

        while True:
            # Título do Jogo
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size = 50, text = "Comida", text_color = (COR_AZUL), text_center_pos = ((WIN_WIDTH / 2), 50))
            self.menu_text(text_size=50, text="Maluca", text_color=(COR_AZUL), text_center_pos=((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size = 30, text = MENU_OPTION[i], text_color = (COR_VERDE), text_center_pos = ((WIN_WIDTH / 2), 180 + 40 * i))

            pygame.display.flip()

            # Check por todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting...")
                    pygame.quit()  # Close Window
                    quit()  # Fecha o pygame

    #Metodo para textos do menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name = "Cooper Black", size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



