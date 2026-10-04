
import pygame
import random
import sys 
from settings import Settings
from game_function import gf
import ship
pygame.init()
def run_game():
  WIDTH=800
  HEIGHT=900
  bg_color=(230,200,300)
  screen.fill(bg_color)
  
  ai_settings=Settings()
  screen=pygame.display.set_mode((
  ai_settings.screen.width,ai_settings.screen_height))

  screen=pygame.display.set_mode((WIDTH,HEIGHT))
  pygame.display.set_caption("zaid invasion")
  
  
  #Make a ship
  ship=Ship(screen)
  
  while True:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
              sys.exit()
              
      ship.blitme()
      screen.fill(ai_settings.bg_color)
      pygame.display.flip()
      screen.fill(ai_settings.bg_color)
      gf.check_events(ai_settings,ship,screen)
      
      ship.update()
      gf.update_screen(ai_settings, screen, ship)
      

run_game()
 
