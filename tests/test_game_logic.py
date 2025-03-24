#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test module for game logic functionality.

This module contains tests for the GameLogic class.
"""

import unittest
from src.game.game_logic import GameLogic

class TestGameLogic(unittest.TestCase):
    """Test cases for the game logic."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.game_logic = GameLogic()
    
    def test_initialize_game(self):
        """Test initializing a new game."""
        min_number = 1
        max_number = 100
        
        # Initialize the game
        self.game_logic.initialize_game(min_number, max_number)
        
        # Check that the secret number is within range
        self.assertIsNotNone(self.game_logic.secret_number)
        self.assertGreaterEqual(self.game_logic.secret_number, min_number)
        self.assertLessEqual(self.game_logic.secret_number, max_number)
    
    def test_check_guess_correct(self):
        """Test checking a correct guess."""
        # Set a known secret number
        self.game_logic.secret_number = 42
        
        # Check a correct guess
        result = self.game_logic.check_guess(42)
        self.assertEqual(result, 0)
    
    def test_check_guess_too_low(self):
        """Test checking a guess that's too low."""
        # Set a known secret number
        self.game_logic.secret_number = 42
        
        # Check a guess that's too low
        result = self.game_logic.check_guess(41)
        self.assertEqual(result, -1)
    
    def test_check_guess_too_high(self):
        """Test checking a guess that's too high."""
        # Set a known secret number
        self.game_logic.secret_number = 42
        
        # Check a guess that's too high
        result = self.game_logic.check_guess(43)
        self.assertEqual(result, 1)
    
    def test_is_valid_guess(self):
        """Test validating guesses."""
        min_number = 1
        max_number = 100
        
        # Test valid guesses
        self.assertTrue(self.game_logic.is_valid_guess(1, min_number, max_number))
        self.assertTrue(self.game_logic.is_valid_guess(50, min_number, max_number))
        self.assertTrue(self.game_logic.is_valid_guess(100, min_number, max_number))
        
        # Test invalid guesses
        self.assertFalse(self.game_logic.is_valid_guess(0, min_number, max_number))
        self.assertFalse(self.game_logic.is_valid_guess(101, min_number, max_number))

if __name__ == '__main__':
    unittest.main()
