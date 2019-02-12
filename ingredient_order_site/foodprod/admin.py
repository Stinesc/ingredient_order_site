from django.contrib import admin
from .models import Dish, Ingredient, Order, DishIngredient, OrderIngredient


class DishAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_time')
    list_filter = ('id', 'data_time')
    search_fields = ('id', 'data_time')


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
