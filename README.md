# Forest Fire Spread Simulation

## Overview

This project simulates the spread of a wildfire using a Cellular Automata (CA) model, incorporating environmental factors such as wind speed, humidity, and tree density. The simulation provides insight into wildfire dynamics for education, analysis, and fire management purposes.

## Features

- Customizable simulation parameters: wind speed, humidity, grid size.
- Real-time visualization of fire spread using Pygame.
- Directional wind bias with probabilistic modeling.
- Quantitative data logging of burned cells, fire duration, and fire front progression.
- Statistical analysis and boxplots of simulation outcomes.

## Technologies Used

- Python 3.9+
- NumPy
- Pygame
- Matplotlib

## Setup Instructions

1. **Create a virtual environment**:  
   `python -m venv .venv`

2. **Activate the virtual environment**:  
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

3. **Install the required dependencies**:  
   `pip install -r requirements.txt`

4. **Run the simulation**:  
   `python main.py`

This will launch the simulation window and begin animating fire spread based on the parameters set in the `config.json` file.

## Project Structure

- `main.py` — Entry point for running the simulation.
- `fire_spread.py` — Handles probabilistic fire spread logic.
- `visualization.py` — Renders the grid and fire animation.
- `log.py` — Logs simulation statistics.
- `weather.py` — Handles environmental influences like wind direction and humidity.
- `config.json` — Configuration file to modify simulation settings.
- `requirements.txt` — List of required Python packages.

## Requirements

- Python 3.9 or higher
- Operating Systems: Windows 10/11 (tested), macOS, Linux
- Basic hardware capable of running Python and Pygame

## Notes

- Always activate the virtual environment before running.
- Data logs are automatically saved in the `/logs/` directory after a simulation run.
- Large grid sizes or extreme parameters may slightly impact performance on lower-end systems.

## Repository
(https://github.com/AColas109/Fire-Simulation)
