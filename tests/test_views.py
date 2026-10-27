from django.test import TestCase
#from capstone.littlelemon.LittleLemon.restaurant.serializers import MenuSerializer
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(
            title="Pizza",
            price=12.99,
            inventory=5
        )

        Menu.objects.create(
            title="Burger",
            price=8.99,
            inventory=10
        )

    def test_get_all(self):
        items = Menu.objects.all()
        #self.assertEqual(len(items), 2) #len(Menu.objects.all())
        serialized_data = MenuSerializer(items, many=True).data
        self.assertEqual(len(serialized_data), 2)