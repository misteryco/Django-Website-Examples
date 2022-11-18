from django.core.exceptions import ValidationError
from django.test import TestCase

from TestingDjango.web.models import Profile


class ProfileModelTest(TestCase):
    # 3A - Arrange, Acct, Assert
    #    - Setup,   Do,   Check Result
    def test_profile_save_when_egn_valid_correct_result(self):
        # Arrange
        profile = Profile(
            name='Don',
            age=19,
            egn=7802127022,
        )

        # Act
        profile.full_clean()
        profile.save()

        # Assert
        self.assertIsNotNone(profile.pk)

    def test_profile_save_when_egn_9_digits_valid_correct_result(self):
        # Arrange
        profile = Profile(
            name='Don',
            age=19,
            egn=780212702,
        )

        with self.assertRaises(ValidationError) as context:
            # Act
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)