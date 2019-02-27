from rest_framework import serializers
from notes.models import Note
from .models import Dish, Ingredient, Order


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('title', 'body', 'creation_datetime', 'author')


class DishSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'author', 'ingredients', 'notes')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'author')
