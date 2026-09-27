from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Apartment


class ApartmentStatisticsAccessTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='owner', password='test-pass')
        self.other_user = User.objects.create_user(username='other', password='test-pass')
        self.apartment = Apartment.objects.create(
            user=self.owner,
            max_people=2,
            sleeping_places=2,
            sleeping_rooms=1,
            bathrooms=1,
            square=50,
            cost_per_night=100,
            prepayment=50,
            min_nights=1,
        )

    def test_owner_can_view_apartment_statistics(self):
        self.client.force_login(self.owner)

        response = self.client.get(reverse('stat', args=[self.apartment.pk]))

        self.assertEqual(response.status_code, 200)

    def test_other_user_cannot_view_apartment_statistics(self):
        self.client.force_login(self.other_user)

        response = self.client.get(reverse('stat', args=[self.apartment.pk]))

        self.assertEqual(response.status_code, 404)
