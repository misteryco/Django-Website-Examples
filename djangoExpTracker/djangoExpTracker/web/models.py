from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils.deconstruct import deconstructible


def chars_only_validator(value):
    if value.isalpha():
        return True
    return ValidationError("Ensure this value contains only letters.")


# Create your models here.
def min_file_size(value):
    file_size_limit = 5 * 1024 * 1024
    if value.size > file_size_limit:
        raise ValidationError('Max file size is 5.00 MB')


@deconstructible
class MaxFileSizeValidator:
    def __init__(self, max_file_size):
        self.max_file_size = max_file_size

    def __call__(self, value):
        filesize = value.file.size
        file_size_limit = self.max_file_size * 1024 * 1024
        if filesize > file_size_limit:
            raise ValidationError(f'Max file size is {self.max_size_mb:.2f} MB')


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            chars_only_validator,

        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            chars_only_validator,

        ]
    )
    budget = models.FloatField(
        default=0,
        validators=(MinValueValidator(0),),
    )

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True,
        validators=[min_file_size, ],
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Expense(models.Model):
    title = models.CharField(max_length=30)

    expense_image = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )
    price = models.FloatField(
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ('title', 'price')
