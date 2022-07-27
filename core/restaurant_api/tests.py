from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestListCreateRestaurant(APITestCase):

    def test_create_restourant(self):
        todo = {'title': "Mac'Donalds"}
        response = self.client.post(reverse('add_restaurant'), todo)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestListMakeVote(APITestCase):

    def test_to_add_to_vote_on_day(self):
        todo = {'menu': '5', 'user': '1'}
        response = self.client.post(reverse('make_vote'), todo)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_to_get_menu(self):
        response = self.client.get(reverse('get_menu'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
