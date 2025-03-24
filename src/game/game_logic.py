#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Game Logic Module

This module contains the GameLogic class which handles the core game mechanics.
"""

import random
import logging

# Set up logging
logger = logging.getLogger(__name__)

class GameLogic:
    """Handles the core game mechanics."""
    
    def __init__(self):
        """Initialize the game logic."""
        self.secret_number = None
        logger.info("Game logic initialized")
    
    def initialize_game(self, min_number, max_number):
        """
        Initialize a new game by selecting a random number.
        
        Args:
            min_number (int): Minimum number in range
            max_number (int): Maximum number in range
        """
        self.secret_number = random.randint(min_number, max_number)
        logger.info(f"New game initialized with range {min_number}-{max_number}")
        logger.debug(f"Secret number set to {self.secret_number}")
    
    def check_guess(self, guess):
        """
        Check if the guess is correct, too high, or too low.
        
        Args:
            guess (int): The player's guess
            
        Returns:
            int: 0 if correct, -1 if too low, 1 if too high
        """
        if guess == self.secret_number:
            return 0
        elif guess < self.secret_number:
            return -1
        else:
            return 1
    
    def is_valid_guess(self, guess, min_number, max_number):
        """
        Check if the guess is valid (within the specified range).
        
        Args:
            guess (int): The player's guess
            min_number (int): Minimum number in range
            max_number (int): Maximum number in range
            
        Returns:
            bool: True if valid, False otherwise
        """
        return min_number <= guess <= max_number
