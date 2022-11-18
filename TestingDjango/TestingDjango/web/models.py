from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

from TestingDjango.web.validators import egn_validator


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(
        validators=(
            validators.MinValueValidator(0),
            validators.MaxValueValidator(150),
        )
    )
    egn = models.CharField(max_length=10, validators=[egn_validator])
