import random
pygame.init

screen_info=pygame.display.info()

size=(width,height)=(int(screen_info.current_w),int(screen_info.current_h))

screen=pygame.display.set_model(size)

clock=pygame.time.clock()

speed=pygame.math.vector2((0,10))
rotate=random.randint(0,360)
speed.rotate_ip(rotate)
fish_image=pygame.transform.rotate(fish_image,180_rotate)

def move_fish():
global speed
fishrect.move_ip(speed)

if fish_rect.left<0 or fish_rect.right>screen_info.current w:
speed[0]*=-1
fish_image=pygame.transform.flip(fish_image,True,False)
fish_rect.move_ip(speed[0],0)

def main():
  while True:
    clock.tick(60)
    screen.fill(65,190,220)
    screen.blit(fish_image)
    pygame.display.flip()