import csv
import os
import time
from fire_spread import BURNING, TREE, EMPTY

class FireLogger:
    def __init__(self, filename="logs/fire_log.csv"):
        self.filename = filename
        self.markdown_file = filename.replace(".csv", ".md")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        self.rows = []
        self.logs = []

    def log_step(self, forest, wind_speed, humidity):
        burning = (forest == BURNING).sum()
        burned = (forest == EMPTY).sum()
        unburned = (forest == TREE).sum()
        total_cells = burning + unburned + burned
        percent_burned = round((burned / total_cells) * 100, 2) if total_cells > 0 else 0

        self.rows.append([
            burning, burned, unburned, percent_burned, wind_speed, humidity
        ])

    def log_config(self, config):
        self.logs.append("\n**Simulation Configuration:**\n")
        for key, value in config.items():
            self.logs.append(f"- **{key}**: `{value}`")
        self.logs.append("")  # Add spacing

    def finalize(self, elapsed_time_ms):
        with open(self.markdown_file, mode="w") as f:
            f.write(f"# Forest Fire Simulation Log\n\n")
            f.write(f"**Total Simulation Time:** `{elapsed_time_ms} ms`\n\n")

            # Write config block if available
            for line in self.logs:
                f.write(line + "\n")
            f.write("\n")

            f.write("| Step | Burning | Burned | Unburned | % Burned | Wind  | Humidity |\n")
            f.write("|------|---------|--------|----------|----------|-------|----------|\n")

            for step, row in enumerate(self.rows):
                burning, burned, unburned, percent, wind, humidity = row
                f.write(f"| {step:>4} | {burning:>7} | {burned:>6} | {unburned:>8} | {percent:>8.2f}% | {wind:<5.1f} | {humidity:<8.1f} |\n")
