from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView, FormView
from .forms import DishIngredientFormSet
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Dish, Ingredient, DishIngredient


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


class DishCreateView(CreateView):
    model = Dish
    fields = ['name', 'description']
    success_url=reverse_lazy('foodprod:index')

    def get_context_data(self, **kwargs):
        context = super(DishCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['dish_ingredient_formset'] = DishIngredientFormSet(self.request.POST)
        else:
            context['dish_ingredient_formset'] = DishIngredientFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['dish_ingredient_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)


class DishUpdateView(UpdateView):
    model = Dish
    fields = ['name', 'description']
    success_url = reverse_lazy('foodprod:index')

    def get_context_data(self, **kwargs):
        context = super(DishUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['dish_ingredient_formset'] = DishIngredientFormSet(self.request.POST, instance=self.object)
            context['dish_ingredient_formset'].full_clean()
        else:
            context['dish_ingredient_formset'] = DishIngredientFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['dish_ingredient_formset']
        print(context['dish_ingredient_formset'])
        if formset.is_valid():
            print('valid')
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            print('not valid')
            return super().form_invalid(form)


class DishDeleteView(DeleteView):
    model = Dish
    success_url = reverse_lazy('foodprod:index')


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
