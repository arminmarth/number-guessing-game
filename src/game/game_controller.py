#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Game Controller Module

This module contains the GameController class which manages the game flow.
"""

import logging
from src.game.game_logic import GameLogic
from src.game.game_ui import GameUI
from src.utils.config import DifficultySettings

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class GameController:
    """Controls the flow of the game."""
    
    def __init__(self):
        """Initialize the game controller."""
        self.ui = GameUI()
        self.game_logic = GameLogic()
        self.wins = 0
        self.losses = 0
        logger.info("Game controller initialized")
    
    def run(self, difficulty='medium', show_instructions=False):
        """
        Run the game.
        
        Args:
            difficulty (str): Difficulty level ('easy', 'medium', 'hard', 'custom')
            show_instructions (bool): Whether to show instructions
            
        Returns:
            int: Exit code (0 for success)
        """
        self.ui.show_welcome()
        
        if show_instructions:
            self.ui.show_instructions()
            
        # Game loop
        play_again = True
        while play_again:
            # Get difficulty settings
            if difficulty == 'custom':
                min_num, max_num, max_attempts = self.ui.get_custom_settings()
            else:
                min_num, max_num, max_attempts = DifficultySettings.get_settings(difficulty)
            
            # Play one game
            result = self.play_game(min_num, max_num, max_attempts)
            if result:
                self.wins += 1
                logger.info(f"Player won. Total wins: {self.wins}")
            else:
                self.losses += 1
                logger.info(f"Player lost. Total losses: {self.losses}")
                
            # Show current stats
            self.ui.show_stats(self.wins, self.losses)
            
            # Ask to play again
            play_again = self.ui.ask_play_again()
        
        self.ui.show_goodbye()
        return 0
    
    def play_game(self, min_num, max_num, max_attempts):
        """
        Play one game.
        
        Args:
            min_num (int): Minimum number in range
            max_num (int): Maximum number in range
            max_attempts (int): Maximum number of attempts allowed
            
        Returns:
            bool: True if player won, False otherwise
        """
        # Initialize the game
        self.game_logic.initialize_game(min_num, max_num)
        secret_number = self.game_logic.secret_number
        attempts = 0
        guessed_numbers = []
        
        logger.info(f"Game initialized with secret number: {secret_number}")
        self.ui.show_game_start(min_num, max_num, max_attempts)
        
        while attempts < max_attempts:
            # Get player's guess
            guess, quit_game = self.ui.get_guess(attempts + 1, max_attempts, min_num, max_num)
            
            # Check if player wants to quit
            if quit_game:
                self.ui.show_game_over(secret_number, guessed_numbers, False)
                return False
                
            # Track this attempt
            attempts += 1
            guessed_numbers.append(guess)
            
            # Check if guess is correct
            if guess == secret_number:
                self.ui.show_win(secret_number, attempts)
                return True
            
            # Provide feedback
            is_low = guess < secret_number
            self.ui.show_feedback(is_low, max_attempts - attempts)
        
        # Player ran out of attempts
        self.ui.show_game_over(secret_number, guessed_numbers, True)
        return False
