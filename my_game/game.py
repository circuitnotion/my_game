import pygame
from settings import SCREEN_HEIGHT,SCREEN_WIDTH,PFS,PLAYER_SPEED
from player import Player
from enemy import Enemey

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("mygame")
    self.clock = pygame.time.Clock()
    self.running = True
    self.all_sprites = pygame.sprite.Group()
    self.enemies = pygame.sprite.Group()
    self.player = Player(100,100)
    self.all_sprites.add(self.player)

    for i in range(3):
      enemy=Enemey(200*i+50,300)
      self.all_sprites.add(enemy)
      self.enemies.add(enemy)
  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False

  def run(self):
    while self.running:
      self.handle_events()
      keys = pygame.key.get_pressed()
      self.player.update(keys)
      self.screen.fill((30,30,30))
      self.all_sprites.draw(self.screen)
      pygame.display.flip()
      self.clock.tick(PFS)
    pygame.quit()