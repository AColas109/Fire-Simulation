import numpy as np
import time
import json
from fire_spread import spread_fire
from visualization import visualize_fire

# Load configuration
with open("config.json", "r") as f:
    config = json.load(f)

GRID_SIZE = (50, 50)
EMPTY, TREE, BURNING = 0, 1, 2

# Initialize forest grid
forest = np.random.choice([TREE, EMPTY], size=GRID_SIZE, p=[config["tree_density"], 1 - config["tree_density"]])
forest[GRID_SIZE[0] // 2, GRID_SIZE[1] // 2] = BURNING  # Start fire in center

def run_simulation(steps=50):
    for step in range(steps):
        forest[:] = spread_fire(forest, config["wind_speed"], config["humidity"])
        visualize_fire(forest)  # Update visualization
        time.sleep(0.1)

if __name__ == "__main__":
    run_simulation()
