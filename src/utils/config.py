#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Configuration Module

This module contains configuration settings for the game.
"""

class DifficultySettings:
    """Difficulty settings for the game."""
    
    @staticmethod
    def get_settings(difficulty):
        """
        Get game settings for a specific difficulty level.
        
        Args:
            difficulty (str): Difficulty level ('easy', 'medium', 'hard')
            
        Returns:
            tuple: (min_number, max_number, max_attempts)
        """
        if difficulty == 'easy':
            return 1, 50, 10
        elif difficulty == 'hard':
            return 1, 200, 5
        else:  # medium (default)
            return 1, 100, 7
