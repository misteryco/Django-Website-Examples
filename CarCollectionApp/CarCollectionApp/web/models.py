from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


# Create your models here.
def between_years_validator(value):
    if not (1980 <= value <= 2049):
        raise ValidationError(f"Year must be between 1980 and 2049")


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        null=False,
        blank=False,
        validators=[
            # min_len_2_validator,
            MinLengthValidator(2, "The username must be a minimum of 2 chars")
        ],
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(18),
        ]
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture'
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif not self.last_name:
            return f"{self.first_name}"
        return f"{self.last_name}"


class Car(models.Model):
    TYPE_MAX_LEN = 10
    MODEL_MAX_LEN = 20

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_TYPE_CHOICES = [
        (SPORTS_CAR, "Sports Car"),
        (PICKUP, "Pickup"),
        (CROSSOVER, "Crossover"),
        (MINIBUS, "Minibus"),
        (OTHER, "Other"),
    ]

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        null=False,
        blank=False,
        choices=CAR_TYPE_CHOICES,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(2),
        ]
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[between_years_validator]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1)]
    )
