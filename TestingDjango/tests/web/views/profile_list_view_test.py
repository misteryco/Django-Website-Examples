from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from TestingDjango.web.models import Profile
from tests.base import BaseTestCase


class ProfileListViewTest(BaseTestCase):
    def test_profiles_list_view__when_no_profiles_expect_empty_list_and_zero_count(self):
        # self.client.get() makes HTTP GET request
        response = self.client.get(reverse('list profiles'))
        # print(response)
        # print(response.context)
        # print(response.template_name)
        self.assertCollectionEmpty(response.context['profile_list'])
        self.assertEqual(0, response.context['profiles_count'])

    def test_profiles_list_view__when_profiles_expect_list_of_profile_and_count(self):
        # Profile creation
        profile_count = 9
        profiles = [
            Profile(
                name=f'Test User {i}',
                age=20 + i,
                egn=f'123456789{i}'
            )
            for i in range(1, profile_count + 1)
        ]
        Profile.objects.bulk_create(profiles)

        response = self.client.get(reverse('list profiles'))
        # print(response)
        # print(response.context)
        # print(response.template_name)
        self.assertListEqual(profiles, list(response.context['profile_list']))
        self.assertEqual(profile_count, response.context['profiles_count'])

    def test_profiles_list_view__when_anonymous_expect_list_of_profile_and_count(self):
        # act
        response = self.client.get(reverse('list profiles'))
        self.assertEqual('Anonymous', response.context['username'])
