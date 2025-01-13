import pygame


class Player(pygame.sprite.Sprite):

  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((50, 50))
    self.image.fill((255, 255, 255))
    self.rect = self.image.get_rect(topleft=(x, y))
    self.speed = 5

  def update(self, keys):
    if keys[pygame.K_UP]:
      self.rect.y -= self.speed
    if keys[pygame.K_DOWN]:
      self.rect.y += self.speed
    if keys[pygame.K_LEFT]:
      self.rect.x -= self.speed
    if keys[pygame.K_RIGHT]:
      self.rect.x += self.speed
