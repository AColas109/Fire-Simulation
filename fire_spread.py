import numpy as np

EMPTY, TREE, BURNING = 0, 1, 2
WIND_BIAS_DIR = (0, 1)  # Wind blowing to the right

def spread_fire(forest, config):
    wind_speed = config.get("wind_speed", 1.0)
    humidity = config.get("humidity", 0.3)
    BASE_SPREAD_PROB = config.get("BASE_SPREAD_PROB", 0.3)
    MAX_SPREAD_PROB = config.get("MAX_SPREAD_PROB", 0.7)

    rows, cols = forest.shape
    new_forest = forest.copy()

    for r in range(rows):
        for c in range(cols):
            if forest[r, c] == BURNING:
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and forest[nr, nc] == TREE:
                        spread_prob = BASE_SPREAD_PROB * wind_speed * (1 - humidity)
                        if (dr, dc) == WIND_BIAS_DIR:
                            spread_prob *= 1.5
                        spread_prob = min(spread_prob, MAX_SPREAD_PROB)
                        spread_prob = max(spread_prob, 0.1)  # Floor to allow fire to spread

                        rand_val = np.random.rand()
                        if rand_val < spread_prob:
                            new_forest[nr, nc] = BURNING
                            print(f"🔥 ({r},{c}) → ({nr},{nc}) | P={spread_prob:.2f} vs Rand={rand_val:.2f}")

    # After spreading, turn burning trees into empty
    for r in range(rows):
        for c in range(cols):
            if forest[r, c] == BURNING:
                new_forest[r, c] = EMPTY

    return new_forest
