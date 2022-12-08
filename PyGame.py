import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My first game')
YELLOW = (255, 255, 153)

done = False  # Loop until the user clicks the close button.
clock = pygame.time.Clock()  # Used to manage how fast the screen updates
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")

    gameDisplay.fill(YELLOW)  # First, clear the screen to white. Don't put other drawing commands

    pygame.display.update()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # Limit to 60 frames per second
