#!/usr/bin/env python3
"""
Number Guessing Game

A simple interactive game where the computer selects a random number
and the player tries to guess it with feedback after each attempt.

Author: Armin Marth (enhanced by Manus Assistant)
Version: 1.1.0
"""

import random
import time
import argparse
import sys

def get_difficulty_settings(difficulty):
    """
    Define game parameters based on difficulty level.
    
    Args:
        difficulty (str): Difficulty level ('easy', 'medium', 'hard', or 'custom')
        
    Returns:
        tuple: (min_number, max_number, max_attempts)
    """
    if difficulty == 'easy':
        return 1, 50, 10
    elif difficulty == 'medium':
        return 1, 100, 7
    elif difficulty == 'hard':
        return 1, 200, 5
    elif difficulty == 'custom':
        try:
            min_num = int(input("Enter minimum number: "))
            max_num = int(input("Enter maximum number: "))
            attempts = int(input("Enter maximum number of attempts: "))
            return min_num, max_num, attempts
        except ValueError:
            print("Invalid input. Using medium difficulty.")
            return 1, 100, 7
    else:
        return 1, 100, 7  # Default to medium

def play_game(min_number, max_number, max_attempts):
    """
    Main game function.
    
    Args:
        min_number (int): Minimum number in range
        max_number (int): Maximum number in range
        max_attempts (int): Maximum number of attempts allowed
        
    Returns:
        bool: True if player won, False otherwise
    """
    # Select a random number
    secret_number = random.randint(min_number, max_number)
    attempts = 0
    guessed_numbers = []
    
    print(f"\nI'm thinking of a number between {min_number} and {max_number}.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        # Get player's guess
        try:
            guess_input = input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ")
            
            # Allow player to quit
            if guess_input.lower() in ('q', 'quit', 'exit'):
                print(f"\nThe number was {secret_number}. Better luck next time!")
                return False
                
            guess = int(guess_input)
            
            # Validate the guess is in range
            if guess < min_number or guess > max_number:
                print(f"Please enter a number between {min_number} and {max_number}.")
                continue
                
            # Track this attempt
            attempts += 1
            guessed_numbers.append(guess)
            
            # Check if guess is correct
            if guess == secret_number:
                print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts!")
                return True
            
            # Provide feedback
            if guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
                
            # Show remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts remaining.")
            
        except ValueError:
            print("Please enter a valid number.")
    
    # Player ran out of attempts
    print(f"\nGame over! You've used all {max_attempts} attempts.")
    print(f"The number was {secret_number}.")
    print(f"Your guesses: {guessed_numbers}")
    return False

def show_stats(wins, losses):
    """Display game statistics."""
    total_games = wins + losses
    if total_games > 0:
        win_percentage = (wins / total_games) * 100
        print(f"\nGame Statistics:")
        print(f"Games Played: {total_games}")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Win Rate: {win_percentage:.1f}%")
    else:
        print("\nNo games played yet.")

def show_instructions():
    """Display game instructions."""
    print("\n=== NUMBER GUESSING GAME INSTRUCTIONS ===")
    print("1. The computer will select a random number within a range.")
    print("2. You need to guess that number within the allowed attempts.")
    print("3. After each guess, you'll get feedback (too high/too low).")
    print("4. Type 'q', 'quit', or 'exit' at any time to end the game.")
    print("5. Different difficulty levels provide different challenges.")
    print("   - Easy: 1-50, 10 attempts")
    print("   - Medium: 1-100, 7 attempts")
    print("   - Hard: 1-200, 5 attempts")
    print("   - Custom: You define the parameters")
    print("6. Have fun and good luck!\n")

def main():
    """Main function to run the game."""
    parser = argparse.ArgumentParser(description='Number Guessing Game')
    parser.add_argument('-d', '--difficulty', choices=['easy', 'medium', 'hard', 'custom'],
                        default='medium', help='Game difficulty level')
    parser.add_argument('-i', '--instructions', action='store_true',
                        help='Show game instructions')
    
    args = parser.parse_args()
    
    print("\n===== NUMBER GUESSING GAME =====")
    
    if args.instructions:
        show_instructions()
        
    # Initialize stats
    wins = 0
    losses = 0
    
    # Game loop
    play_again = True
    while play_again:
        min_num, max_num, max_attempts = get_difficulty_settings(args.difficulty)
        
        # Play one game
        if play_game(min_num, max_num, max_attempts):
            wins += 1
        else:
            losses += 1
            
        # Show current stats
        show_stats(wins, losses)
        
        # Ask to play again
        while True:
            again = input("\nWould you like to play again? (y/n): ").lower()
            if again in ('y', 'yes'):
                break
            elif again in ('n', 'no'):
                play_again = False
                break
            else:
                print("Please enter 'y' or 'n'.")
    
    print("\nThanks for playing Number Guessing Game!")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        sys.exit(1)
