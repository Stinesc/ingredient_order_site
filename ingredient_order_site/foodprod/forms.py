from django.forms.models import inlineformset_factory
from .models import Dish, DishIngredient, Ingredient


DishIngredientFormSet = inlineformset_factory(Dish, DishIngredient, fields=['ingredient', 'quantity'], exclude=[],
                                              extra=Ingredient.objects.count(), max_num=Ingredient.objects.count(),
                                              can_delete=False)
