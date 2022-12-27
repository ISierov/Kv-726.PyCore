import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

pygame.init ()

size = [700, 500]                                               # put the size of our screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Happy New Year")

done = False                                                    # make loop till click to close

clock = pygame.time.Clock()                                     # screen update



snowflake_list = []
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    snowflake_list.append ([x, y])



while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    for item in snowflake_list:
        item[1] += 1
        pygame.draw.circle(screen, WHITE, item, 2)

        if item[1] > 500:                                       # loop making new items appear
            item[1] = random.randrange(-30, -7)
            item[0] = random.randrange(700)

    pygame.display.flip()
    clock.tick(20)                                            # 20/sec

pygame.QUIT()                                                 # the end