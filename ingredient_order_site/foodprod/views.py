from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView, FormView
from django.views.generic.edit import ModelFormMixin
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Dish, Ingredient, DishIngredient
from .forms import DishForm


class IndexView(ListView):
    template_name = "foodprod/index.html"
    model = Dish

    def get_queryset(self):
        search_query = self.request.GET.get('search_query')
        if search_query:
            object_list = self.model.objects.filter(Q(name__icontains=search_query) |
                                                    Q(description__icontains=search_query))
        else:
            object_list = self.model.objects.all()
        return object_list


class DishDetailView(DetailView):
    template_name = "foodprod/dish.html"
    model = Dish


class DishCreateView(FormView):
    template_name = "foodprod/dish_form.html"
    form_class = DishForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        ingredients = form.cleaned_data['ingredients']
        dish = Dish(name=name, description=description)
        dish.save()
        ingredient_list = Ingredient.objects.filter(pk__in=ingredients)
        for ingredient in ingredient_list:
            dish_ingredient = DishIngredient()
            dish_ingredient.dish = dish
            dish_ingredient.ingredient = ingredient
            dish_ingredient.quantity = form.cleaned_data[str(ingredient.pk)]
            dish_ingredient.save()
        return super(ModelFormMixin, self).form_valid(form)

    '''model = Dish
    fields = ['name', 'description', 'ingredients']

    def form_valid(self, form):
        print('sdfsd')
        self.object = form.save(commit=False)
        for ingredient in form.cleaned_data['ingredients']:
            dish_ingredient = DishIngredient()
            dish_ingredient.dish = self.object
            dish_ingredient.ingredient = ingredient
            dish_ingredient.save()
            print(ingredient)
        return super(ModelFormMixin, self).form_valid(form)'''


class IngredientsListView(ListView):
    template_name = "foodprod/ingredients.html"
    model = Ingredient


class IngredientDetailView(DetailView):
    template_name = "foodprod/ingredient.html"
    model = Ingredient


class IngredientCreateView(CreateView):
    model = Ingredient
    fields = ['name']


class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ['name']
    success_url = reverse_lazy('foodprod:ingredients')


class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('foodprod:ingredients')
