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
        self.client.post(reverse('foodprod:order_create'), {'dish_id': self.dish.id})
        self.assertEquals(Order.objects.count(), orders_count + 1)

    def test_order_add_invalid(self):
        orders_count = Order.objects.count()
        self.client.post(reverse('foodprod:order_create'), {'dish_id': self.dish_invalid.id})
        self.assertNotEquals(Order.objects.count(), orders_count + 1)


class AddIngredientToDishTestCase(TestCase):

    def setUp(self):
        self.dish = Dish.objects.create(name="some_dish", description="Some_dish")
        self.ingredient = Ingredient.objects.create(name="some_ingredient")

    def test_add_ingredient_valid(self):
        data = {'csrfmiddlewaretoken': 'yURYMNdCcYkNDwMZk7oQ5J4rcJ10pII8oZFLChWzpjYcj4x8lkhPwyV9S9k6W8jy0',
                'name': 'some_dish',
                'description': 'Some_dish',
                'dishingredient_set-INITIAL_FORMS': '0',
                'dishingredient_set-TOTAL_FORMS': '1',
                'dishingredient_set-MAX_NUM_FORMS': '7',
                'dishingredient_set-MIN_NUM_FORMS': '0',
                'dishingredient_set-0-ingredient': self.ingredient.id,
                'dishingredient_set-0-quantity': '1',
                'dishingredient_set-0-dish': self.dish.id,
                'dishingredient_set-0-id': ''}
        count_before_add = DishIngredient.objects.count()
        dish_update_url = reverse('foodprod:dish_update', kwargs={'pk': self.dish.id})
        response = self.client.post(dish_update_url, data)
        count_after_add = DishIngredient.objects.count()
        self.assertEqual(count_before_add+1, count_after_add)
        self.assertEqual(response.status_code, 302)

    def test_add_ingredient_invalid(self):
        data = {'csrfmiddlewaretoken': 'yURYMNdCcYkNDwMZk7oQ5J4rcJ10pII8oZFLChWzpjYcj4x8lkhPwyV9S9k6W8jy0',
                'name': 'some_dish',
                'description': 'Some_dish',
                'dishingredient_set-INITIAL_FORMS': '0',
                'dishingredient_set-TOTAL_FORMS': '1',
                'dishingredient_set-MAX_NUM_FORMS': '7',
                'dishingredient_set-MIN_NUM_FORMS': '0',
                'dishingredient_set-0-ingredient': self.ingredient.id,
                'dishingredient_set-0-quantity': '',
                'dishingredient_set-0-dish': self.dish.id,
                'dishingredient_set-0-id': ''}
        count_before_add = DishIngredient.objects.count()
        dish_update_url = reverse('foodprod:dish_update', kwargs={'pk': self.dish.id})
        response = self.client.post(dish_update_url, data)
        count_after_add = DishIngredient.objects.count()
        self.assertNotEqual(count_before_add+1, count_after_add)
        self.assertEqual(response.status_code, 200)
