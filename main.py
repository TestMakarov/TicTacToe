import pygame
import minimax
from tkinter import *
import tkinter.messagebox
from pygame.locals import *

# Constants

# converting colors to RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (222, 105, 88)
BLUE = (120, 191, 197)
GRAY = (61, 64, 76)
GRAY2 = (134, 137, 143)

# squares size
WIDTH = 100
HEIGHT = 100

MARGIN = 5

WINDOW_SIZE = [320, 320]

FPS = 60

# -------- Main Program Loop -----------


def main():
    # initializing main screen
    global grid, screen, flag, FPSClock, root
    # we need two next lines to create messagebox
    root = Tk()
    root.withdraw()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(WHITE)
    pygame.display.set_caption("Tic-Tac-Toe")
    pygame.init()
    FPSClock = pygame.time.Clock()

    # creating and initializing game grid
    grid = []
    for row in range(3):
        grid.append([])
        for column in range(3):
            grid[row].append(0)
    # setting flag for defining players turn
    flag = 1

    while True:
        run()


def run():
    global flag, game
    # game is a string perfomance of game grid
    game = ""
    check_for_player_step()
    if not flag:
        ai_step()

    # drawing game elements
    show_elements()
    FPSClock.tick(FPS)
    pygame.display.flip()

    # checking for win or quit
    check_for_win(game)
    check_for_quit()


def check_for_player_step():
    global grid, flag

    # waiting until player press on somehow square
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # getting mouse position
            pos = pygame.mouse.get_pos()

            # converting mouse position into cell of grid matrix
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (WIDTH + MARGIN)

            # setting cell of grid matrix as "x"
            grid[row][column] = 1

            # changing turn (ai's turn)
            flag = not flag


def ai_step():
    global flag, game
    game = ""

    # converting game grid into string to process data by ai
    for row in range(3):
        for column in range(3):
            if grid[row][column] == 0:
                game += "-"
            elif grid[row][column] == 1:
                game += "x"
            else:
                game += "o"

    # checking whether it's the last turn
    if game.count("-") >= 2:
        game = minimax.get(game)

    # converting processed string to game grid
    for row in range(3):
        for column in range(3):
            if game[3 * row + column] == "x":
                grid[row][column] = 1
            elif game[3 * row + column] == "o":
                grid[row][column] = 2
            else:
                grid[row][column] = 0

    # changing turn (player's turn)
    flag = not flag


def show_elements():
    for row in range(3):
        for column in range(3):
            if grid[row][column] == 2:
                # if zero might be in the cell drawing circle and changing square's background
                pygame.draw.rect(screen, GRAY, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN,
                                 WIDTH, HEIGHT])
                pygame.draw.circle(screen, GRAY2, [((MARGIN + WIDTH) * column + MARGIN) // 2 + 52 * (column + 1),
                                                   ((MARGIN + HEIGHT) * row + MARGIN) // 2 + 52 * (row+1)], 30, 6)

            elif grid[row][column] == 1:
                # if cross might be here drawing cross and changing square's background
                pygame.draw.rect(screen, RED, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN,
                                 WIDTH, HEIGHT])

                # drawing cross by two lines
                pygame.draw.line(screen, WHITE, [((MARGIN + WIDTH) * column + MARGIN) + 25,
                                                 ((MARGIN + HEIGHT) * row + MARGIN) + 30],
                                 [((MARGIN + WIDTH) * (column + 1) + MARGIN)-35,
                                  ((MARGIN + HEIGHT) * (row + 1) + MARGIN) - 30], 12)
                pygame.draw.line(screen, WHITE, [((MARGIN + WIDTH) * (column + 1) + MARGIN)-35,
                                                 ((MARGIN + HEIGHT) * row + MARGIN) + 30], [((MARGIN + WIDTH) * column
                                                                                             + MARGIN)+25,
                                                                                            ((MARGIN + HEIGHT) * (
                                                                                                        row + 1) +
                                                                                             MARGIN) - 30], 12)
            else:
                # if the positon is free drawing square
                pygame.draw.rect(screen, BLUE, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN,
                                 WIDTH, HEIGHT])


def check_for_quit():
    for event in pygame.event.get((QUIT, KEYUP)):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def check_for_win(game):
    # if all cells are free
    if len(game) == 0:
        return

    # processing all posible win combinations
    if (game[0] == game[1] == game[2] == "o") or (game[3] == game[4] == game[5] == "o") \
            or (game[6] == game[7] == game[8] == "o") or (game[0] == game[3] == game[6] == "o") \
            or (game[1] == game[4] == game[7] == "o") or (game[2] == game[5] == game[8] == "o") \
            or (game[0] == game[4] == game[8] == "o") or (game[2] == game[4] == game[6] == "o"):
        tkinter.messagebox.showinfo("LoseAlert", "You Lose!")
        main()
    elif (game[0] == game[1] == game[2] == "x") or (game[3] == game[4] == game[5] == "x") \
            or (game[6] == game[7] == game[8] == "x") or (game[0] == game[3] == game[6] == "x") \
            or (game[1] == game[4] == game[7] == "x") or (game[2] == game[5] == game[8] == "x") \
            or (game[0] == game[4] == game[8] == "x") or (game[2] == game[4] == game[6] == "x"):
        # this code will never execute (it's impossible to win this game)
        tkinter.messagebox.showinfo("WinAlert", "You Win!")
        main()

    # if there is no free cells anymore
    elif game.count("-") == 0:
        tkinter.messagebox.showinfo("DrawAlert", "Draw!")
        main()


if __name__ == "__main__":
    main()
