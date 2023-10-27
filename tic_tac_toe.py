import pygame, sys
import numpy as np

pygame.init()

# figures colors
RED = (255, 0, 0)

# Screen coordinates
WIDTH = 600
HEIGHT = 600

# board rows and cols
BOARD_ROWS = 3
BOARD_COLS = 3

# Lines color, width
LINE_COLOR = (23, 145, 135)
LINE_WIDTH = 15

# Back ground color
BG_COLOR = (28, 170, 156)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# title, screen color in RGB format
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# board filled with zeros
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# Draw game lines
def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (20, 200), (580, 200), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (20, 400), (580, 400), LINE_WIDTH)

    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (200, 20), (200, 580), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (400, 20), (400, 580), LINE_WIDTH)

def draw_figs():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(col * 200 + 100 / 2)), (int(row * 200 + 100 / 2)) )


# mark square with values in the board
def mark_square(row, col, player):
    board[row][col] = player

# check if there is empty squares in the board
def avilable_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

# check if board if full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True


draw_lines()

player = 1

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # link console board with the screen board
        if event.type == pygame.MOUSEBUTTONDOWN:
           mouseX = event.pos[0] # x
           mouseY = event.pos[1] # y

           clicked_row = int(mouseY // 200)
           clicked_col = int(mouseX // 200)

           if avilable_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, player)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, player)
                    player = 1
                print(board)

    # update screen
    pygame.display.update()
