#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Game UI Module

This module contains the GameUI class which handles user interaction.
"""

import logging

# Set up logging
logger = logging.getLogger(__name__)

class GameUI:
    """Handles user interaction for the game."""
    
    def show_welcome(self):
        """Display welcome message."""
        print("\n===== NUMBER GUESSING GAME =====")
        logger.info("Welcome message displayed")
    
    def show_instructions(self):
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
        logger.info("Instructions displayed")
    
    def show_game_start(self, min_num, max_num, max_attempts):
        """
        Display game start message.
        
        Args:
            min_num (int): Minimum number in range
            max_num (int): Maximum number in range
            max_attempts (int): Maximum number of attempts allowed
        """
        print(f"\nI'm thinking of a number between {min_num} and {max_num}.")
        print(f"You have {max_attempts} attempts to guess it.\n")
        logger.info(f"Game start message displayed for range {min_num}-{max_num}")
    
    def get_guess(self, current_attempt, max_attempts, min_num, max_num):
        """
        Get the player's guess.
        
        Args:
            current_attempt (int): Current attempt number
            max_attempts (int): Maximum number of attempts allowed
            min_num (int): Minimum number in range
            max_num (int): Maximum number in range
            
        Returns:
            tuple: (guess, quit_flag) where guess is the player's guess (int) and
                  quit_flag (bool) indicates if the player wants to quit
        """
        while True:
            try:
                guess_input = input(f"Attempt {current_attempt}/{max_attempts}. Enter your guess: ")
                
                # Check if player wants to quit
                if guess_input.lower() in ('q', 'quit', 'exit'):
                    logger.info("Player chose to quit")
                    return None, True
                    
                guess = int(guess_input)
                
                # Validate the guess is in range
                if guess < min_num or guess > max_num:
                    print(f"Please enter a number between {min_num} and {max_num}.")
                    continue
                
                logger.info(f"Player guessed {guess}")
                return guess, False
                
            except ValueError:
                print("Please enter a valid number.")
                logger.warning("Invalid input received")
    
    def show_feedback(self, is_low, remaining_attempts):
        """
        Display feedback after a guess.
        
        Args:
            is_low (bool): True if the guess was too low, False if too high
            remaining_attempts (int): Number of attempts remaining
        """
        if is_low:
            print("Too low!")
        else:
            print("Too high!")
            
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts remaining.")
        
        logger.info(f"Feedback provided: {'Too low' if is_low else 'Too high'}")
    
    def show_win(self, secret_number, attempts):
        """
        Display win message.
        
        Args:
            secret_number (int): The secret number
            attempts (int): Number of attempts used
        """
        print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts!")
        logger.info(f"Player won in {attempts} attempts")
    
    def show_game_over(self, secret_number, guessed_numbers, used_all_attempts):
        """
        Display game over message.
        
        Args:
            secret_number (int): The secret number
            guessed_numbers (list): List of guessed numbers
            used_all_attempts (bool): True if player used all attempts, False if quit
        """
        if used_all_attempts:
            print(f"\nGame over! You've used all your attempts.")
        else:
            print(f"\nThe number was {secret_number}. Better luck next time!")
            
        print(f"The number was {secret_number}.")
        print(f"Your guesses: {guessed_numbers}")
        logger.info("Game over message displayed")
    
    def show_stats(self, wins, losses):
        """
        Display game statistics.
        
        Args:
            wins (int): Number of wins
            losses (int): Number of losses
        """
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
        
        logger.info(f"Stats displayed: {wins} wins, {losses} losses")
    
    def ask_play_again(self):
        """
        Ask if the player wants to play again.
        
        Returns:
            bool: True if player wants to play again, False otherwise
        """
        while True:
            again = input("\nWould you like to play again? (y/n): ").lower()
            if again in ('y', 'yes'):
                logger.info("Player chose to play again")
                return True
            elif again in ('n', 'no'):
                logger.info("Player chose not to play again")
                return False
            else:
                print("Please enter 'y' or 'n'.")
    
    def show_goodbye(self):
        """Display goodbye message."""
        print("\nThanks for playing Number Guessing Game!")
        logger.info("Goodbye message displayed")
    
    def get_custom_settings(self):
        """
        Get custom difficulty settings from the player.
        
        Returns:
            tuple: (min_number, max_number, max_attempts)
        """
        print("\n=== Custom Difficulty Settings ===")
        
        while True:
            try:
                min_number = int(input("Enter minimum number: "))
                max_number = int(input("Enter maximum number: "))
                
                if min_number >= max_number:
                    print("Maximum number must be greater than minimum number.")
                    continue
                
                max_attempts = int(input("Enter maximum attempts: "))
                
                if max_attempts <= 0:
                    print("Maximum attempts must be greater than 0.")
                    continue
                
                logger.info(f"Custom settings: range {min_number}-{max_number}, {max_attempts} attempts")
                return min_number, max_number, max_attempts
                
            except ValueError:
                print("Please enter valid numbers.")
                logger.warning("Invalid input for custom settings")
