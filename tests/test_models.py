from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Pizza', price=10.99, inventory=5)
        self.assertEqual(str(item), 'Pizza : 10.99')