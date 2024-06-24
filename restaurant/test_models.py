from django.test import TestCase
from restaurant import models

class MenuTest(TestCase):
    def test_create_item(self):
        menu = models.Menu.objects.create(ID=3, Title="Makhani Pizza", Price=25, Inventory=10)
        self.assertEqual(str(menu), "Makhani Pizza : 25")

