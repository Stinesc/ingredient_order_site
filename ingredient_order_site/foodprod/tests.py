from django.test import TestCase, Client
from .models import Dish, DishIngredient, Order, OrderIngredient
from django.urls import reverse
from .models import Dish, Ingredient


class OrderCreateTestCase(TestCase):

    def setUp(self):
        self.dish = Dish.objects.create(name="lollipop", description="Tasty lollipop")
        self.ingredient1 = Ingredient.objects.create(name="sugar")
        self.ingredient2 = Ingredient.objects.create(name="water")
        self.dish_ingredient1 = DishIngredient.objects.create(dish=self.dish, ingredient=self.ingredient1, quantity=100)
        self.dish_ingredient2 = DishIngredient.objects.create(dish=self.dish, ingredient=self.ingredient2, quantity=300)
        self.dish_invalid = Dish.objects.create(name="invalid dish", description="Anything invalid dish")

    def test_orders_template(self):
        response = self.client.get(reverse('foodprod:orders'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'foodprod/orders.html')

    def test_order_add_valid(self):
        orders_count = Order.objects.count()
        order_create_url = reverse('foodprod:order_create', kwargs={'dish_id' : self.dish.id})
        self.client.get(order_create_url)
        self.assertEquals(Order.objects.count(), orders_count + 1)

    def test_order_add_invalid(self):
        orders_count = Order.objects.count()
        order_create_url = reverse('foodprod:order_create', kwargs={'dish_id' : self.dish_invalid.id})
        self.client.get(order_create_url)
        self.assertNotEquals(Order.objects.count(), orders_count + 1)


class AddIngredientToDishTestCase(TestCase):

    def setUp(self):
        Dish.objects.create(name="some dish", description="Some dish")
        Ingredient.objects.create(name="some ingredient")

    def test_add_ingredient_valid(self):
        dish = Dish.objects.filter(name="some dish").first()
        dish_update_url = reverse('foodprod:dish_update',kwargs={'pk': dish.id})
        data = {'form-TOTAL_FORMS': ['1'],
                'form-MIN_NUM_FORMS': ['0'],
                'form-INITIAL_FORMS': ['0'],
                'form-0-ingredient': ['some ingredient'],
                'form-0-quantity': ['1.0'],
                'form-0-id': ['']}
        count_before_add = DishIngredient.objects.filter(dish__name="some dish").count()
        response = self.client.post(dish_update_url, data)
        count_after_add = DishIngredient.objects.filter(dish__name="some dish").count()
        self.assertEqual(count_before_add+1, count_after_add)
        self.assertEqual(response.status_code, 302)
