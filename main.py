import numpy as np
import time
import json
from fire_spread import spread_fire, EMPTY, TREE, BURNING
from visualization import visualize_fire
from log import FireLogger

# Load configuration from file
with open("config.json", "r") as f:
    config = json.load(f)

GRID_SIZE = tuple(config.get("grid_size", [50, 50]))

# Initialize forest with all trees
forest = np.full(GRID_SIZE, TREE, dtype=np.uint8)
# Set initial burning cell in center
center_r, center_c = GRID_SIZE[0] // 2, GRID_SIZE[1] // 2
forest[center_r, center_c] = BURNING

def run_simulation(steps=50):
    log = FireLogger()
    log.log_config(config)
    start_time = time.time()

    for step in range(steps):
        forest[:] = spread_fire(forest, config)
        log.log_step(forest, config["wind_speed"], config["humidity"])
        visualize_fire(forest)
        time.sleep(0.1)

    elapsed_time_ms = round((time.time() - start_time) * 1000)
    log.finalize(elapsed_time_ms)

if __name__ == "__main__":
    run_simulation()
