pygame.init
screen_info=pygame.display.info()
size=(width,height)=(int(screen_info.current_w),int(screen_info.current_h))
screen=pygame.display.set_model(size)
clock=pygame.time.clock()

def main():
  while True:
    clock.tick(60)
    screen.fill(65,190,220)
    screen.blit(fish_image)
    pygame.display.flip()