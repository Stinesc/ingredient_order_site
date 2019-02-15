from django.forms.models import inlineformset_factory
from .models import Dish, Order, Ingredient, DishIngredient, OrderIngredient


DishIngredientFormSet = inlineformset_factory(Dish, DishIngredient, fields=['ingredient', 'quantity'], exclude=[],
                                              extra=5, max_num=7, can_delete=False)

OrderIngredientFormSet = inlineformset_factory(Order, OrderIngredient, fields=['ingredient', 'quantity'], exclude=[],
                                              extra=0, can_delete=False)
