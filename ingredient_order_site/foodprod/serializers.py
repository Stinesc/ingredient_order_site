from rest_framework import serializers

from notes.models import Note, NoteItem
from .models import Dish, Ingredient

from notes.serializers import NoteSerializer


class DishSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'author', 'ingredients', 'notes')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'author')
