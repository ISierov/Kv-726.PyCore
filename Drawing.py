import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((600, 600))

def three_in_raw(arr):
    if arr[0][0] == arr[0][1] == arr[0][2]:
        return arr[0][0]
    if arr[0][0] == arr[1][1] == arr[2][2]:
        return arr[0][0]
    if arr[0][0] == arr[1][0] == arr[2][0]:
        return arr[0][0]
    if arr[0][1] == arr[1][1] == arr[2][1]:
        return arr[0][1]
    if arr[0][2] == arr[1][2] == arr[2][2]:
        return arr[0][2]
    if arr[1][0] == arr[1][1] == arr[1][2]:
        return arr[1][0]
    if arr[2][0] == arr[2][1] == arr[2][2]:
        return arr[2][0]
    if arr[2][0] == arr[1][1] == arr[0][2]:
        return arr[2][0]
    return False

pygame.display.set_caption('My drawing')
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

step = 0  # even = 0, odd = X

arr = [[100, 101, 102], [200, 201, 202], [300, 301, 302]]

done = False  # Loop until the user clicks the close button.
clock = pygame.time.Clock()  # Used to manage how fast the screen updates
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif pygame.key.get_pressed()[pygame.K_1]:
            if arr[0][0] == 'X' or arr[0][0] == 'O':
                continue
            else:
                arr[0][0] = 'X' if step % 2 == 1 else 'O'
                step += 1
                if three_in_raw(arr) == 'X':
                    print('X is winner!')
                    done = True
                elif three_in_raw(arr) == 'O':
                    print('O is winner!')
                    done = True

        elif pygame.key.get_pressed()[pygame.K_2]:
            if arr[0][1] == 'X' or arr[0][1] == 'O':
                continue
            else:
                arr[0][1] = 'X' if step % 2 == 1 else 'O'
                step += 1
                if three_in_raw(arr) == 'X':
                    print('X is winner!')
                    done = True
                elif three_in_raw(arr) == 'O':
                    print('O is winner!')
                    done = True

        elif pygame.key.get_pressed()[pygame.K_3]:
            if arr[0][2] == 'X' or arr[0][2] == 'O':
                continue
            else:
                arr[0][2] = 'X' if step % 2 == 1 else 'O'
                step += 1
                if three_in_raw(arr) == 'X':
                    print('X is winner!')
                    done = True
                elif three_in_raw(arr) == 'O':
                    print('O is winner!')
                    done = True

        elif pygame.key.get_pressed()[pygame.K_4]:
            if arr[1][0] == 'X' or arr[1][0] == 'O':
                continue
            else:
                arr[1][0] = 'X' if step % 2 == 1 else 'O'
                step += 1
                if three_in_raw(arr) == 'X':
                    print('X is winner!')
                    done = True
                elif three_in_raw(arr) == 'O':
                    print('O is winner!')
                    done = True

        elif pygame.key.get_pressed()[pygame.K_5]:
            if arr[1][1] == 'X' or arr[1][1] == 'O':
                continue
            else:
                arr[1][1] = 'X' if step % 2 == 1 else 'O'
                step += 1
                if three_in_raw(arr) == 'X':
                    print('X is winner!')
                    done = True
                elif three_in_raw(arr) == 'O':
                    print('O is winner!')
                    done = True

        elif pygame.key.get_pressed()[pygame.K_6]:
            if arr[1][2] == 'X' or arr[1][2] == 'O':
                continue
            else:
                arr[1][2] = 'X' if step % 2 == 1 else 'O'
                step += 1
                if three_in_raw(arr) == 'X':
                    print('X is winner!')
                    done = True
                elif three_in_raw(arr) == 'O':
                    print('O is winner!')
                    done = True

        elif pygame.key.get_pressed()[pygame.K_7]:
            if arr[2][0] == 'X' or arr[2][0] == 'O':
                continue
            else:
                arr[2][0] = 'X' if step % 2 == 1 else 'O'
                step += 1
                if three_in_raw(arr) == 'X':
                    print('X is winner!')
                    done = True
                elif three_in_raw(arr) == 'O':
                    print('O is winner!')
                    done = True

        elif pygame.key.get_pressed()[pygame.K_8]:
            if arr[2][1] == 'X' or arr[2][1] == 'O':
                continue
            else:
                arr[2][1] = 'X' if step % 2 == 1 else 'O'
                step += 1
                if three_in_raw(arr) == 'X':
                    print('X is winner!')
                    done = True
                elif three_in_raw(arr) == 'O':
                    print('O is winner!')
                    done = True

        elif pygame.key.get_pressed()[pygame.K_9]:
            if arr[2][2] == 'X' or arr[2][2] == 'O':
                continue
            else:
                arr[2][2] = 'X' if step % 2 == 1 else 'O'
                step += 1
                if three_in_raw(arr) == 'X':
                    print('X is winner!')
                    done = True
                elif three_in_raw(arr) == 'O':
                    print('O is winner!')
                    done = True

    gameDisplay.fill(WHITE)  # First, clear the screen to white. Don't put other drawing commands

    pygame.draw.line(gameDisplay, BLACK, (200, 0), (200, 600), 5)
    pygame.draw.line(gameDisplay, BLACK, (400, 0), (400, 600), 5)
    pygame.draw.line(gameDisplay, BLACK, (0, 200), (600, 200), 5)
    pygame.draw.line(gameDisplay, BLACK, (0, 400), (600, 400), 5)


    def draw_O(i, j):
        pygame.draw.circle(gameDisplay, BLUE, (i*200+100, j*200+100), 90, width=10)

    def draw_X(i, j):
        pygame.draw.line(gameDisplay, RED, (i*200, j*200), (i*200+200, j*200+200), 5)
        pygame.draw.line(gameDisplay, RED, (i*200+200, j*200), (i*200, j*200+200), 5)

    for i in range(3):
        for j in range(3):
            if arr[i][j] == 'O':
                draw_O(i, j)
            elif arr[i][j] == 'X':
                draw_X(i, j)
            else:
                continue

    # font = pygame.font.SysFont('Comic Sans', 25, True, False)
    # text = font.render("My text", True, BLACK, RED)
    # gameDisplay.blit(text, (10, 500))

    # pygame.draw.aaline(gameDisplay, RED, (100, 100), (400, 300), 5)
    # pygame.draw.rect(gameDisplay, BLACK, [55, 50, 20, 25])
    # pygame.draw.circle(gameDisplay, BLUE, (500, 500), 50, width=10, draw_bottom_right=True, draw_top_left=True)
    # pygame.draw.circle(gameDisplay, RED, (500, 500), 50, width=10, draw_bottom_left=True, draw_top_right=True)
    pygame.display.update()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # Limit to 60 frames per second
