from rest_framework import serializers
from notes.models import Note
from .models import Dish, Ingredient, Order, DishIngredient, OrderIngredient


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('title', 'body', 'creation_datetime', 'author')


class DishIngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = DishIngredient
        fields = ('id', 'ingredient', 'quantity')


class OrderIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.CharField(source='ingredient.name')

    class Meta:
        model = OrderIngredient
        fields = ('id', 'ingredient', 'quantity')


class DishSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)
    ingredients = DishIngredientSerializer(source='dishingredient_set', many=True)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'author', 'ingredients', 'notes')

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        dish = Dish.objects.create(**validated_data)
        for track_data in ingredients_data:
            Ingredient.objects.create(dish=dish, **track_data)
        return dish


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'author')


class OrderSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)
    ingredients = DishIngredientSerializer(source='orderingredient_set', many=True)

    class Meta:
        model = Order
        fields = ('id', 'creation_datetime', 'is_active', 'author', 'ingredients', 'notes')
