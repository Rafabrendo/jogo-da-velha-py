import pygame

#pygame setup
pygame.init()
WINDOW_WIDTH = 720
PIXEL_WIDTH = WINDOW_WIDTH // 3
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Jogo da Velha")

def load_icon(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

ICON_X = load_icon('icons/x-icon.png', [PIXEL_WIDTH, PIXEL_WIDTH])
ICON_O = load_icon('icons/o-icon.png', [PIXEL_WIDTH, PIXEL_WIDTH])
GRID = load_icon('icons/grid.png', [WINDOW_WIDTH, WINDOW_WIDTH])
player = 0

def play_turn(current_player):
    curr_coordinate = pygame.math.Vector2(pygame.mouse.get_pos()) // WINDOW_WIDTH
    if pygame.mouse.get_pressed()[0]:
        col, row  = map(int, curr_coordinate)
        board[row][col] = 0 if current_player == 0 else 1
        global player
        player = 1 - player

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    #RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    #Render your game

    screen.blit(GRID, (0, 0))
    screen.blit(ICON_X, (0, 0))
    screen.blit(ICON_O, (WINDOW_WIDTH // 3, WINDOW_WIDTH // 3))
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()