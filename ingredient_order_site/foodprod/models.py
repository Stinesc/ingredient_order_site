from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from notes.models import NoteItem
from django.utils.translation import ugettext as _


class Dish(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=32, unique=True)
    description = models.CharField(verbose_name=_('Description'), max_length=256, blank=True, default="")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField('Ingredient', verbose_name=_('Ingredient'), through='DishIngredient')
    notes = GenericRelation(NoteItem)

    def __str__(self):
        return _(self.name)

    class Meta:
        ordering = ['name']


class Ingredient(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=32, unique=True)
    author = models.ForeignKey(User, verbose_name=_('Author'), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return _(self.name)

    class Meta:
        ordering = ['name']


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(verbose_name=_('Creation datetime'), auto_now_add=True)
    is_active = models.BooleanField(verbose_name=_('Is active'), default=True)
    author = models.ForeignKey(User, verbose_name=_('Author'), on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField('Ingredient', through='OrderIngredient')
    notes = GenericRelation(NoteItem)

    def __str__(self):
        return _(str(self.id))

    class Meta:
        ordering = ['-creation_datetime']


class DishIngredient(models.Model):
    dish = models.ForeignKey('Dish', verbose_name=_('Dish'), on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, related_name='dish_ingredient', blank=True,
                                   null=True)
    quantity = models.FloatField(verbose_name=_('Quantity'), default=0.0, blank=True, null=True)

    def __str__(self):
        return f"Dish: {self.dish} <> Ingredient: {self.ingredient} <> Quantity: {self.quantity}"


class OrderIngredient(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', verbose_name=_('Ingredients'), on_delete=models.CASCADE, related_name='order_ingredients', blank=True,
                                   null=True)
    quantity = models.FloatField(verbose_name=_('Quantity'), default=0.0, blank=True, null=True)

    def __str__(self):
        return f"Order: {self.order} <> Ingredient: {self.ingredient}"
