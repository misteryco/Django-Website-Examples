from random import choices

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.forms import CharField


# Create your models here.

class Profile(models.Model):
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,

        # validators=[MinValueValidator(12)]
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_MAX_LEN,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=LAST_NAME_MAX_LEN,
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORIES_MAX_LEN = 15

    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD = "Board/Card Game"
    OTHER = "Other"

    CATEGORIES_CHOICES = [
        (ACTION, "Action"),
        (ADVENTURE, "Adventure"),
        (PUZZLE, "Puzzle"),
        (STRATEGY, "Strategy"),
        (SPORTS, "Sports"),
        (BOARD_CARD, "Board/Card Game"),
        (OTHER, "Other"),
    ]

    title = models.CharField(
        null=False,
        blank=False,
        max_length=TITLE_MAX_LEN,
        unique=True,
    )
    category = models.CharField(
        max_length=CATEGORIES_MAX_LEN,
        choices=CATEGORIES_CHOICES,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        ]
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
        verbose_name='Max Level'
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
