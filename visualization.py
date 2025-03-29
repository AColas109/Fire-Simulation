import pygame
import numpy as np

CELL_SIZE = 10
WHITE, GREEN, RED, BLACK = (255, 255, 255), (34, 139, 34), (255, 0, 0), (0, 0, 0)

pygame.init()
screen = None  # This will be initialized only once

def visualize_fire(forest):
    global screen
    rows, cols = forest.shape

    # Initialize the screen only once (for performance)
    if screen is None:
        screen = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE))

    screen.fill(WHITE)

    for r in range(rows):
        for c in range(cols):
            state = forest[r, c]
            color = BLACK if state == 0 else GREEN if state == 1 else RED
            pygame.draw.rect(screen, color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

# Test mode
if __name__ == "__main__":
    dummy_forest = np.random.choice([0, 1, 2], size=(80, 120))
    visualize_fire(dummy_forest)
    pygame.time.wait(2000)
