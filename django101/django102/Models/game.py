from django.db import models

from django102.Models.player import Player


class Game(models.Model):
    EASY = 1
    MEDIUM = 2
    HARD = 3

    DIFFICULTY_LEVELS_CHOICES =(
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard')
    )

    name = models.CharField(max_length=30, blank=False, default='')
    level_of_difficulty = models.CharField(
        max_length=2,
        blank=False,
        choices=DIFFICULTY_LEVELS_CHOICES,
        default=MEDIUM,
    )
    players = models.ManyToManyField(Player)