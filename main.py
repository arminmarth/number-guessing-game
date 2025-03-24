#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Number Guessing Game - Main Module

This is the main entry point for the Number Guessing Game.
It handles command-line arguments and starts the game.
"""

import sys
import argparse
from src.game.game_controller import GameController

def main():
    """Main function to run the game."""
    parser = argparse.ArgumentParser(description='Number Guessing Game')
    parser.add_argument('-d', '--difficulty', 
                        choices=['easy', 'medium', 'hard', 'custom'],
                        default='medium', 
                        help='Game difficulty level')
    parser.add_argument('-i', '--instructions', 
                        action='store_true',
                        help='Show game instructions')
    
    args = parser.parse_args()
    
    # Create and run the game controller
    game = GameController()
    return game.run(args.difficulty, args.instructions)

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        sys.exit(1)
