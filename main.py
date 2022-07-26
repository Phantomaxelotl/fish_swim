import random
import pygame
import sys
from pygame.locals import*
pygame.init

screen_info=pygame.display.info()

size=(width,height)=(int(screen_info.current_w),int(screen_info.current_h))

screen=pygame.display.set_model(size)

clock=pygame.time.clock()



fish_image=pygame.image.load("fish.png")
fish_image=pygame.transform.smoothscale(fish_image(80,80))
fish_rect=fish_image.get_rect()
fish_rect.center=(width//2,height//2)


speed.rotate_ip(rotate)
fish_image=pygame.transform.rotate(fish_image,180-rotate)

speed=pygame.math.vector2((0,10))
rotate=random.randint(0,360)
speed.rotate_ip(rotate)
fish_image=pygame.transform.rotate(fish_image,180-rotate)

def move_fish():
  global speed, fish_image
  fishrect.move_ip(speed)

  screen_info=pygame.display.Info()
  fish_rect.move_ip(speed)
  
  if fish_rect.left<0 or fish_rect.right>screen_info.current_w:
    speed[0]*=-1
    fish_image=pygame.transform.flip(fish_image,True,False)
    fish_rect.move_ip(speed[0],0)
  
  def main():
    while True:
      clock.tick(60) #refresh game page every second
      for event in pygame.event.get():
        if event.type == QUIT:
          sys.exit()

      
      screen.fill(65,190,220)
      screen.blit(fish_image) #blit display fish
      pygame.display.flip()
  if __nmae__ == "__main__":
    main()