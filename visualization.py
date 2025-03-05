import pygame
import numpy as np

GRID_SIZE = (50, 50)
CELL_SIZE = 10
WHITE, GREEN, RED, BLACK = (255, 255, 255), (34, 139, 34), (255, 0, 0), (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((GRID_SIZE[1] * CELL_SIZE, GRID_SIZE[0] * CELL_SIZE))

def visualize_fire(forest):
    screen.fill(WHITE)
    
    for r in range(GRID_SIZE[0]):
        for c in range(GRID_SIZE[1]):
            color = BLACK if forest[r, c] == 0 else GREEN if forest[r, c] == 1 else RED
            pygame.draw.rect(screen, color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

if __name__ == "__main__":
    dummy_forest = np.random.choice([0, 1, 2], size=GRID_SIZE)
    visualize_fire(dummy_forest)
    pygame.time.wait(2000)
 