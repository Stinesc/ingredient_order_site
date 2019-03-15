from django.contrib import admin
from .models import Dish, Ingredient, Order, DishIngredient, OrderIngredient


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'author')
    list_filter = ('name', 'author')
    search_fields = ('name', 'author')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    list_filter = ('name', 'author')
    search_fields = ('name', 'author')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'creation_datetime', 'author', 'is_active')
    list_filter = ('id', 'creation_datetime', 'author', 'is_active')
    search_fields = ('id', 'creation_datetime', 'author')


class DishIngredientAdmin(admin.ModelAdmin):
    list_display = ('dish', 'ingredient', 'quantity')
    list_filter = ('dish', 'ingredient',)
    search_fields = ('dish__name', 'ingredient__name')


class OrderIngredientAdmin(admin.ModelAdmin):
    list_display = ('order', 'ingredient', 'quantity')
    list_filter = ('order', 'ingredient')
    search_fields = ('order__id', 'ingredient__name')


admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(DishIngredient, DishIngredientAdmin)
admin.site.register(OrderIngredient, OrderIngredientAdmin)
