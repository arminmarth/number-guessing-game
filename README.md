# Number Guessing Game

A fun interactive game where the computer selects a random number and the player tries to guess it with feedback after each attempt.

## Features

- Multiple difficulty levels (Easy, Medium, Hard, Custom)
- Feedback after each guess (too high/too low)
- Game statistics tracking
- Command-line arguments for customization
- Comprehensive error handling

## Installation

No installation required beyond Python 3.6+. The script uses only standard library modules.

```bash
# Clone the repository
git clone https://github.com/arminmarth/number-guessing-game.git
cd number-guessing-game

# Make the script executable (optional)
chmod +x number_guessing_game.py
```

## Usage

```bash
python number_guessing_game.py [options]
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

Play with default settings (medium difficulty):
```bash
python number_guessing_game.py
```

Play on easy difficulty:
```bash
python number_guessing_game.py --difficulty easy
```

Show instructions before playing:
```bash
python number_guessing_game.py --instructions
```

## How to Play

1. The computer will select a random number within a range based on the difficulty level
2. You need to guess that number within the allowed attempts
3. After each guess, you'll get feedback (too high/too low)
4. Type 'q', 'quit', or 'exit' at any time to end the current game
5. After each game, you'll see your statistics and can choose to play again

## Game Rules

- You must enter a valid number within the specified range
- Each guess counts as an attempt
- You win if you guess the correct number within the allowed attempts
- You lose if you use all attempts without guessing correctly

## License

This project is open source and available under the MIT License.
