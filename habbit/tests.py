from rest_framework import status
from rest_framework.test import APITestCase

from habbit.models import Habbit
from users.models import User
from django.urls import reverse


class HabbitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='test',
            password='test'
        )
        self.client.force_authenticate(user=self.user)
        self.habbit = Habbit.objects.create(
            user=self.user,
            place='Квартира',
            time="10:00:00",
            action='Йога',
            useful=True,
            period=1,
            time_complete=10
        )

    def test_create_habit(self):
        url = reverse('habbit:habbit-create')
        data = {
            'user': self.user.id,
            'place': 'Стадион',
            'time': '08:00:00',
            'action': 'Бег',
            'useful': False,
            'period': 8,
            'time_complete': 15
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habbit.objects.count(), 2)

    def test_list_habits(self):
        url = reverse('habbit:habbit-list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_habit(self):
        url = reverse('habbit:habbit-get', args=[self.habbit.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'], 'Квартира')

    def test_update_habit(self):
        url = reverse('habbit:habbit-update', args=[self.habbit.id])
        data = {'place': 'Офис'}
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'], 'Офис')

    def test_destroy_habbit(self):
        url = reverse('habbit:habbit-delete', args=[self.habbit.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habbit.objects.count(), 0)
