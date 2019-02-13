from django import forms
from .models import Ingredient


class DishForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    ingredients = forms.ModelMultipleChoiceField(Ingredient.objects.all())
    #quantity = forms.FloatField()
