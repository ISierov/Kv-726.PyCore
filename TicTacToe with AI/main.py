import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((600, 600))


def three_in_raw(arr, depth, status):  # if status AI, hence this is evaluation function for minimax
    for row in range(3):
        if arr[row][0] == arr[row][1] and arr[row][1] == arr[row][2]:
            if arr[row][0] == 'X':
                return 10-depth if status == "AI" else arr[row][0]
            elif arr[row][0] == 'O':
                return depth-10 if status == "AI" else arr[row][0]

    for col in range(3):
        if arr[0][col] == arr[1][col] and arr[1][col] == arr[2][col]:
            if arr[0][col] == 'X':
                return 10-depth if status == "AI" else arr[0][col]
            elif arr[0][col] == 'O':
                return depth-10 if status == "AI" else arr[0][col]

    if arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2]:
        if arr[0][0] == 'X':
            return 10-depth if status == "AI" else arr[0][0]
        elif arr[0][0] == 'O':
            return depth-10 if status == "AI" else arr[0][0]

    if arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0]:
        if arr[0][2] == 'X':
            return 10-depth if status == "AI" else arr[0][2]
        elif arr[0][2] == 'O':
            return depth-10 if status == "AI" else arr[0][2]

    return 0 if status == "AI" else False


def check_endgame(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == '_':
                return True
    return False


def check_winner(arr):
    if three_in_raw(arr, 0, "Player") == 'X':
        print('AI is winner!')
        return "True"
    elif three_in_raw(arr, 0, "Player") == 'O':
        print('You are winner!')
        return "True"
    return "False"


def main_draw_condition(x, y):
    global arr, step
    if arr[x][y] == 'X' or arr[x][y] == 'O':
        return "continue"
    else:
        arr[x][y] = 'X' if step % 2 == 1 else 'O'
        step += 1
        return check_winner(arr)


def done_condition(flag):
    return False if flag == "False" else True


def minimax(arr, depth, isMax, score):
    new_score = three_in_raw(arr, depth, "AI")

    if isMax and new_score > score:
        return new_score

    if not isMax and new_score < score:
        return new_score

    if check_endgame(arr) == False:
        return 0

    if isMax:
        best = -1000

        for i in range(3):
            for j in range(3):
                if arr[i][j] == '_':
                    arr[i][j] = 'X'
                    best = max(best, minimax(arr, depth + 1, not isMax, new_score))
                    arr[i][j] = '_'
        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if arr[i][j] == '_':
                    arr[i][j] = 'O'
                    best = min(best, minimax(arr, depth + 1, not isMax, new_score))
                    arr[i][j] = '_'
        return best


def findBestMove(arr):  # means AI best move
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):
            if arr[i][j] == '_':
                arr[i][j] = 'X'
                score = three_in_raw(arr, 0, "AI")
                # print("Score is: ", score)
                moveVal = minimax(arr, 0, False, score)
                # print(f"MoveVal[{i}][{j}]: {moveVal}\n")
                arr[i][j] = '_'
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    # print()
    # print("The value of the best Move is: ", bestVal)
    return bestMove


pygame.display.set_caption('My drawing')
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

step = 0  # even = 0, odd = X

arr = [['_', '_', '_'],
       ['_', '_', '_'],
       ['_', '_', '_']]

done = False  # Loop until the user clicks the close button.
clock = pygame.time.Clock()  # Used to manage how fast the screen updates
while not done:
    done = True if step == 9 else False

    if step % 2 == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif pygame.key.get_pressed()[pygame.K_1]:
                flag = main_draw_condition(0, 0)
                if flag == "continue":
                    continue
                done = done_condition(flag)

            elif pygame.key.get_pressed()[pygame.K_2]:
                flag = main_draw_condition(1, 0)
                if flag == "continue":
                    continue
                done = done_condition(flag)

            elif pygame.key.get_pressed()[pygame.K_3]:
                flag = main_draw_condition(2, 0)
                if flag == "continue":
                    continue
                done = done_condition(flag)

            elif pygame.key.get_pressed()[pygame.K_4]:
                flag = main_draw_condition(0, 1)
                if flag == "continue":
                    continue
                done = done_condition(flag)

            elif pygame.key.get_pressed()[pygame.K_5]:
                flag = main_draw_condition(1, 1)
                if flag == "continue":
                    continue
                done = done_condition(flag)

            elif pygame.key.get_pressed()[pygame.K_6]:
                flag = main_draw_condition(2, 1)
                if flag == "continue":
                    continue
                done = done_condition(flag)

            elif pygame.key.get_pressed()[pygame.K_7]:
                flag = main_draw_condition(0, 2)
                if flag == "continue":
                    continue
                done = done_condition(flag)

            elif pygame.key.get_pressed()[pygame.K_8]:
                flag = main_draw_condition(1, 2)
                if flag == "continue":
                    continue
                done = done_condition(flag)

            elif pygame.key.get_pressed()[pygame.K_9]:
                flag = main_draw_condition(2, 2)
                if flag == "continue":
                    continue
                done = done_condition(flag)

    else:  # AI moves
        best_move = findBestMove(arr)
        # print(f"Best Move is : ({best_move[0]}, {best_move[1]})")
        # print()
        flag = main_draw_condition(best_move[0], best_move[1])
        done = done_condition(flag)

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

    pygame.display.update()  # Go ahead and update the screen with what we've drawn.

    clock.tick(60)  # Limit to 60 frames per second
