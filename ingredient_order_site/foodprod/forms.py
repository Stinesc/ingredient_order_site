from django.forms.models import inlineformset_factory
from django.forms import BaseInlineFormSet
from .models import Dish, Order, DishIngredient, OrderIngredient
from django.core.exceptions import ValidationError


class BaseIngredientFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        total_quantity = sum(f.cleaned_data['quantity'] for f in self.forms if f.cleaned_data.get('quantity') is not None)
        if total_quantity <= 0:
            raise ValidationError("Total quantity must be above 0", code='invalid')


DishIngredientFormSet = inlineformset_factory(Dish, DishIngredient, fields=['ingredient', 'quantity'], exclude=[],
                                              formset=BaseIngredientFormSet, extra=5, max_num=7, can_delete=True)

OrderIngredientFormSet = inlineformset_factory(Order, OrderIngredient, fields=['ingredient', 'quantity'], exclude=[],
                                              formset=BaseIngredientFormSet, extra=0, can_delete=True)
