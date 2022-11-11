from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator


class MaxSizeValidator(MaxValueValidator):
    def __init__(self, limit_value):
        super().__init__(self, limit_value)
        self.limit_value = limit_value

    def __call__(self, value):
        # get the file size as cleaned value
        cleaned = self.clean(value.size)
        params = {'limit_value': self.limit_value, 'show_value': cleaned, 'value': value}
        message = f'The file exceed the maximum size of {self.limit_value}s MB.'
        if self.compare(cleaned, self.limit_value * 1024 * 1024):  # convert limit_value from MB to Bytes
            raise ValidationError(self.message, code=self.code, params=params)
