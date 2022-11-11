from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible


# Create your models here.
def contain_coma(value):
    if ' ' in value:
        if ', ' not in value:
            raise ValidationError("Ingredients should be divided by comma !")


@deconstructible
class MoreThanLimit(object):
    def __init__(self, limit):
        self.limit = limit

    def __call__(self, value):
        if len(value) < self.limit:
            raise ValidationError(f'Must be more than {self.limit}m.')
        return value


class Recipe(models.Model):
    TITLE_MAX_LEN = 30
    INGREDIENTS_MAX_LEN = 250

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        validators=[MoreThanLimit(2), MinValueValidator(1)]
    )

    image_url = models.URLField(
        verbose_name="Image URL",
    )

    description = models.TextField()

    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LEN,
        validators=[contain_coma, ]
    )

    time = models.IntegerField(
        validators=[MinValueValidator(0), ],
        verbose_name="Time (Minutes)"
    )
