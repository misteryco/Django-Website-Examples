from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
import re

# Create your models here.
'''
•	Profile
o	Username
	Character field, required.
	 It should have at least 2 characters and maximum - 15 characters.
	The username can consist only of letters, numbers, and underscore ("_"). Otherwise, raise a ValidationError with the
    message: "Ensure this value contains only letters, numbers, and underscore."
o	Email
	Email field, required.
o	Age
	Integer field, optional.
	The age cannot be below 0.



'''


def only_letters_numbers_and_underscore(value):
    pattern = "^[A-Za-z0-9_]*$"  # regex check pattern
    if not bool(re.match(pattern, value)):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 15

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(USERNAME_MIN_LEN),
            only_letters_numbers_and_underscore,
        ],
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )


'''
•	Album
o	Album Name
	Character field, required.
	All album names must be unique.
	 It should consist of a maximum of 30 characters.
o	Artist
	Character field, required.
	It should consist of a maximum of 30 characters.
o	Genre
	Char field, required.
	It should consist of a maximum of 30 characters.
	The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", and "Other".
o	Description
	Text field, optional.
o	Image URL
	URL field, required.
o	Price
	Float field, required.
	The number of decimal places of the price should not be specified in the database.
	The price cannot be below 0.0.

'''


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_NAME_MAX_LEN = 30
    GENRE_NAME_MAX_LEN = 30
    POP = "Pop"
    JAZZ = "Jazz"
    RB = "R&B"
    ROCK = "Rock"
    COUNTRY = "Country"
    DANCE = "Dance"
    HIPHOP = "HipHop"
    OTHER = "Other"

    GENRES = [
        (POP, "Pop Music"),
        (JAZZ, "Jazz Music"),
        (RB, "R&B Music"),
        (ROCK, "Rock Music"),
        (COUNTRY, "Country Music"),
        (DANCE, "Dance Music"),
        (HIPHOP, "Hip Hop Music"),
        (OTHER, "Other")
    ]

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        blank=False,
        null=False,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LEN,
        blank=False,
        null=False,
    )
    genre = models.CharField(
        max_length=GENRE_NAME_MAX_LEN,
        choices=GENRES,
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(0)]
    )
