# Ursina 3D Game

A 3D game built using the Ursina game engine in Python, featuring a first-person controller and dynamic environment elements.

## Features

- First-person controller with customizable mouse sensitivity and movement speed
- Dynamic sky dome with sunset texture
- Water and waterfall effects
- Custom models and textures

## Project Structure

```
├── main.py           # Main game entry point
├── water.py          # Water effects implementation
├── waterfall.py      # Waterfall mechanics
├── walf.py           # Additional game mechanics
├── models/           # 3D model assets
├── textures/         # Texture files
└── functions/        # Utility functions and game setup
    ├── setup.py
    ├── settings.py
    └── utils.py
```

## Requirements

- Python 3.x
- Ursina Engine
- Additional dependencies (specified in requirements)

## Setup

1. Install Python 3.x if not already installed
2. Install the required dependencies:
   ```bash
   pip install ursina
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## Controls

- WASD - Movement
- Mouse - Look around
- Space - Jump
- Left Shift - Run
