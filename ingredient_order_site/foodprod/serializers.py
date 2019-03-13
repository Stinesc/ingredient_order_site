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
        fields = ('ingredient', 'quantity')


class OrderIngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderIngredient
        fields = ('ingredient', 'quantity')


class DishSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)
    ingredients = DishIngredientSerializer(source='dishingredient_set', many=True)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'author', 'ingredients', 'notes')

    def create(self, validated_data):
        ingredients_data = validated_data.pop('dishingredient_set')
        dish = Dish.objects.create(name=validated_data.pop('name'), description=validated_data.pop('description'),
                                   author=validated_data.pop('author'))
        for track_data in ingredients_data:
            DishIngredient.objects.create(dish=dish, **track_data)
        return dish


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'author')


class OrderSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)
    ingredients = OrderIngredientSerializer(source='orderingredient_set', many=True)

    class Meta:
        model = Order
        fields = ('id', 'creation_datetime', 'is_active', 'author', 'ingredients', 'notes')

    def create(self, validated_data):
        orders_data = validated_data.pop('orderingredient_set')
        order = Order.objects.create(is_active=validated_data.pop('is_active'), author=validated_data.pop('author'))
        for track_data in orders_data:
            OrderIngredient.objects.create(order=order, **track_data)
        return order
