# Tetris

A simple offline Tetris game built with Python and Pygame.

The project includes:

- a playable Tetris game loop
- next piece preview
- hold piece support
- ghost piece preview
- local best score saving

## Requirements

- Python 3.10+ recommended
- `pygame`

## Installation

Create a virtual environment if you want, then install the dependencies:

```bash
pip install -r requirements.txt
```

## Run

From the project root:

```bash
python3 main.py
```

## Controls

- `Enter`: start the game from the menu
- `Esc`: quit from the menu
- `Left Arrow`: move piece left
- `Right Arrow`: move piece right
- `Down Arrow`: soft drop
- `Up Arrow`: rotate piece
- `Space`: hard drop
- `C`: hold or swap the current piece

## Local Save Data

This game is fully offline.

The personal best score is saved locally in:

```text
data/scores.json
```

If the file or folder does not exist yet, the game creates it automatically.

## Project Structure

```text
.
├── data/
│   └── scores.json
├── requirements.txt
├── tetris/
│   ├── board.py
│   ├── constants.py
│   ├── game.py
│   ├── menu.py
│   ├── pieces.py
│   ├── renderer.py
│   └── users.py
├── main.py
└── README.md
```

## Notes

- The game stores only local profile data and best score.
- No internet connection is required.
- The project is meant to stay lightweight and easy to extend.
