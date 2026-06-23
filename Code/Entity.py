from abc import abstractmethod, ABC


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load("./Asset/FundoPraiaLevel1.png")
        self.rect = self.surf.get_rect(left = 0, top = 0)
        self.speed = 0

    @abstractmethod
    def move(self):
        pass