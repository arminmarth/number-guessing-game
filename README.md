# Number Guessing Game

A fun interactive game where the computer selects a random number and the player tries to guess it with feedback after each attempt.

## Features

- Multiple difficulty levels (Easy, Medium, Hard, Custom)
- Feedback after each guess (too high/too low)
- Game statistics tracking
- Command-line arguments for customization
- Comprehensive error handling
- Logging system for debugging
- Modular code architecture

## Screenshots

```
===== NUMBER GUESSING GAME =====

I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it.

Attempt 1/7. Enter your guess: 50
Too low!
You have 6 attempts remaining.
Attempt 2/7. Enter your guess: 75
Too high!
You have 5 attempts remaining.
Attempt 3/7. Enter your guess: 62
Too low!
You have 4 attempts remaining.
Attempt 4/7. Enter your guess: 68
Too high!
You have 3 attempts remaining.
Attempt 5/7. Enter your guess: 65
Too high!
You have 2 attempts remaining.
Attempt 6/7. Enter your guess: 63
Too low!
You have 1 attempts remaining.
Attempt 7/7. Enter your guess: 64

Congratulations! You guessed the number 64 in 7 attempts!

Game Statistics:
Games Played: 1
Wins: 1
Losses: 0
Win Rate: 100.0%

Would you like to play again? (y/n): n

Thanks for playing Number Guessing Game!
```

## Installation

### Requirements

- Python 3.8 or higher

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/arminmarth/number-guessing-game.git
   cd number-guessing-game
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Run the game with default settings (medium difficulty):

```bash
python main.py
```

### Command Line Options

```
  -h, --help            Show this help message and exit
  -d {easy,medium,hard,custom}, --difficulty {easy,medium,hard,custom}
                        Game difficulty level (default: medium)
  -i, --instructions    Show game instructions
```

### Difficulty Levels

- **Easy**: Numbers from 1-50, 10 attempts allowed
- **Medium**: Numbers from 1-100, 7 attempts allowed
- **Hard**: Numbers from 1-200, 5 attempts allowed
- **Custom**: You define the range and number of attempts

### Examples

Play on easy difficulty:
```bash
python main.py --difficulty easy
```

Show instructions before playing:
```bash
python main.py --instructions
```

Play on hard difficulty:
```bash
python main.py --difficulty hard
```

## Project Structure

- `main.py` - Application entry point
- `src/` - Source code directory
  - `game/` - Game-related modules
    - `game_controller.py` - Controls game flow
    - `game_logic.py` - Core game mechanics
    - `game_ui.py` - User interface
  - `utils/` - Utility modules
    - `config.py` - Configuration settings
- `tests/` - Unit tests
- `requirements.txt` - Python dependencies
- `LICENSE` - MIT License

## Development

### Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=src
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).
