import pygame
import random

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        tamanho = random.randint(60, 160)
        
        self.image = pygame.image.load("data/asteroide.png")
        self.image = pygame.transform.scale(self.image, [tamanho, tamanho])
        self.rect = self.image.get_rect()
        fator_colisao = int(tamanho * -0.5) 
        self.rect.inflate_ip(fator_colisao, fator_colisao)
        self.rect.x = 840 + random.randint(10, 210)
        self.rect.y = random.randint(2, 450)

        base_speed = (200 / tamanho) + (random.random() * 2)
        self.speed_x = base_speed
        self.speed_y = random.choice([-1.5, -0.5, 0, 0.5, 1.5]) * (random.random() + 0.5)

    def update(self, *args):
        self.rect.x -= self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right < 0 or self.rect.bottom < -50 or self.rect.top > 650:
            self.kill()