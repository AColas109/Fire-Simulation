import pygame

WHITE, GREEN, RED, BLACK = (255, 255, 255), (34, 139, 34), (255, 0, 0), (0, 0, 0)

pygame.init()
screen = None  # Initialize later based on forest shape

def get_cell_size(grid_shape, max_dim=800):
    return max(4, max_dim // max(grid_shape))

def visualize_fire(forest):
    global screen
    rows, cols = forest.shape
    cell_size = get_cell_size((rows, cols))

    if screen is None:
        screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))

    screen.fill(WHITE)

    for r in range(rows):
        for c in range(cols):
            color = BLACK if forest[r, c] == 0 else GREEN if forest[r, c] == 1 else RED
            pygame.draw.rect(screen, color, (c * cell_size, r * cell_size, cell_size, cell_size))

    pygame.display.flip()
