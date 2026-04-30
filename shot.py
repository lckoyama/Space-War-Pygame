import pygame

class Shot(pygame.sprite.Sprite):
    # receber o X e o Y
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        
        self.image = pygame.image.load("data/shot.png")
        self.image = pygame.transform.scale(self.image, [10, 10])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # velocidade do shot
        self.speed = 15

    def update(self, *args):
        # move
        self.rect.x += self.speed
        if self.rect.left > 840:
            self.kill()