import numpy as np

EMPTY, TREE, BURNING = 0, 1, 2

def spread_fire(forest, wind_speed, humidity):
    new_forest = forest.copy()
    rows, cols = forest.shape

    for r in range(rows):
        for c in range(cols):
            if forest[r, c] == BURNING:
                new_forest[r, c] = EMPTY  # Burnt tree turns to empty

                # Spread probability formula
                spread_prob = 0.5 * wind_speed * (1 - humidity)

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and forest[nr, nc] == TREE:
                        if np.random.rand() < spread_prob:
                            new_forest[nr, nc] = BURNING

    return new_forest
