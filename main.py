import pygame
import minimax

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 100
HEIGHT = 100
FPS = 60
MARGIN = 5

grid = []
for row in range(3):
    grid.append([])
    for column in range(3):
        grid[row].append(0)
pygame.init()

WINDOW_SIZE = [320, 320]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic-Tac-Toe")
gameOver = False
flag = 1
FPSClock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not gameOver:
    game = ""
    pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (WIDTH + MARGIN)
            grid[row][column] = 1
            flag = not flag
            pressed = True
    screen.fill(BLACK)
    if not flag and pressed:
        for row in range(3):
            for column in range(3):
                if grid[row][column] == 0:
                    game += "-"
                elif grid[row][column] == 1:
                    game += "x"
                else:
                    game += "o"
        game = minimax.get(game)
        for row in range(3):
            for column in range(3):
                if game[3*row + column] == "x":
                    grid[row][column] = 1
                elif game[3*row + column] == "o":
                    grid[row][column] = 2
                else:
                    grid[row][column] = 0
        flag = not flag
    for row in range(3):
        for column in range(3):
            pygame.draw.rect(screen,
                             WHITE,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            if grid[row][column] == 2:
                pygame.draw.circle(screen, BLACK, [column * (50 + MARGIN * column)+50 * (column+1),
                                                   row * (50 + MARGIN * row) + 50*(row+1)],50, 5)
            elif grid[row][column] == 1:
                pygame.draw.line(screen, BLACK, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN], [(MARGIN + WIDTH) * (column + 1) + MARGIN,
                              (MARGIN + HEIGHT) * (row + 1) + MARGIN], 5)
                pygame.draw.line(screen, BLACK, [(MARGIN + WIDTH) * (column + 1) + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN], [(MARGIN + WIDTH) * column + MARGIN,
                                                 (MARGIN + HEIGHT) * (row + 1) + MARGIN], 5)
    FPSClock.tick(FPS)
    pygame.display.flip()
pygame.quit()