from django.test import TestCase
from restaurant import models
from rest_framework.test import APIClient
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = models.Menu.objects.create(ID=4, Title="Red Sauce Pasta", Price=5, Inventory=50)
        self.menu2 = models.Menu.objects.create(ID=3, Title="Pizza Pocket", Price=2, Inventory=50)

    def test_getall(self):
        
        client = APIClient()
        url = reverse('menu_item_list')
        response = client.get(url)

        expected_data = [{'ID': '3', 'Title': 'Pizza Pocket', 'Price': '2.00', 'Inventory': '50'}, {'ID': '4', 'Title': 'Red Sauce Pasta', 'Price':'5.00', 'Inventory': '50'}]

        self.assertEqual(response.data, expected_data)