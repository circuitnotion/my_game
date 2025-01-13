import pygame
class Enemey(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    super().__init__()
    self.image = pygame.Surface((50, 50))  # Placeholder for enemy sprite
    self.image.fill((255, 0, 0))  # Red
    self.rect = self.image.get_rect(topleft=(x, y))
    self.speed = 2

  def update(self):
    self.rect.x += self.speed
    if self.rect.right > 800 or self.rect.left < 0:
        self.speed *= -1  # Reverse direction