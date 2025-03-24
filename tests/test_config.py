#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test module for configuration functionality.

This module contains tests for the DifficultySettings class.
"""

import unittest
from src.utils.config import DifficultySettings

class TestDifficultySettings(unittest.TestCase):
    """Test cases for the difficulty settings."""
    
    def test_easy_difficulty(self):
        """Test easy difficulty settings."""
        min_num, max_num, max_attempts = DifficultySettings.get_settings('easy')
        self.assertEqual(min_num, 1)
        self.assertEqual(max_num, 50)
        self.assertEqual(max_attempts, 10)
    
    def test_medium_difficulty(self):
        """Test medium difficulty settings."""
        min_num, max_num, max_attempts = DifficultySettings.get_settings('medium')
        self.assertEqual(min_num, 1)
        self.assertEqual(max_num, 100)
        self.assertEqual(max_attempts, 7)
    
    def test_hard_difficulty(self):
        """Test hard difficulty settings."""
        min_num, max_num, max_attempts = DifficultySettings.get_settings('hard')
        self.assertEqual(min_num, 1)
        self.assertEqual(max_num, 200)
        self.assertEqual(max_attempts, 5)

if __name__ == '__main__':
    unittest.main()
