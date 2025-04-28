import numpy as np
import math

EMPTY, TREE, BURNING = 0, 1, 2

# All 8 directional offsets (Moore neighborhood)
MOORE_OFFSETS = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),          (0, 1),
                 (1, -1),  (1, 0),  (1, 1)]

def spread_fire(forest, config):
    wind_speed = config["wind_speed"]
    humidity = config["humidity"]
    BASE_SPREAD_PROB = config["BASE_SPREAD_PROB"]
    MAX_SPREAD_PROB = config["MAX_SPREAD_PROB"]
    wind_dir_deg = config.get("wind_direction_deg", 0)
    wind_rad = math.radians(wind_dir_deg)

    rows, cols = forest.shape
    new_forest = forest.copy()

    for r in range(rows):
        for c in range(cols):
            if forest[r, c] == BURNING:
                for dr, dc in MOORE_OFFSETS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and forest[nr, nc] == TREE:
                        # Compute direction angle
                        spread_angle = math.atan2(dr, dc)
                        angle_diff = abs(spread_angle - wind_rad)
                        angle_diff = min(angle_diff, 2 * math.pi - angle_diff)

                        # Bias for wind alignment (cosine-based)
                        direction_bias = 1.5 + 0.5 * math.cos(angle_diff)

                        # Final spread probability
                        spread_prob = BASE_SPREAD_PROB * wind_speed * (1 - humidity) * direction_bias
                        spread_prob = min(spread_prob, MAX_SPREAD_PROB)

                        if np.random.rand() < spread_prob:
                            new_forest[nr, nc] = BURNING

    # Burnout phase
    for r in range(rows):
        for c in range(cols):
            if forest[r, c] == BURNING:
                new_forest[r, c] = EMPTY

    return new_forest