import pygame
import random

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
       
        self.image = pygame.image.load("data/asteroide.png")
        self.image = pygame.transform.scale(self.image, [150, 150])
        
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-100, -100)
        
        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(2, 400)

        # velocidade random
        self.speed = 1 + random.random() * 2

    def update(self, *args):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()