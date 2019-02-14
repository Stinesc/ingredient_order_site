from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=256, blank=True, default="")
    ingredients = models.ManyToManyField('Ingredient', through='DishIngredient')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Ingredient(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    data_time = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField('Ingredient', through='OrderIngredient')

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['-data_time']


class DishIngredient(models.Model):
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, related_name='dish_ingredient', blank=True,
                                   null=True)
    quantity = models.FloatField(default=0.0, blank=True, null=True)

    def __str__(self):
        return f"Dish: {self.dish} <> Ingredient: {self.ingredient} <> Quantity: {self.quantity}"

    class Meta:
        auto_created = True


class OrderIngredient(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, related_name='order_ingredients', blank=True,
                                   null=True)
    quantity = models.FloatField(default=1.0, blank=True, null=True)

    def __str__(self):
        return f"Order: {self.order} <> Ingredient: {self.ingredient}"
