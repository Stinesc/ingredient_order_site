from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView, TemplateView
from django.views import View
from django.shortcuts import redirect
from .forms import DishIngredientFormSet, OrderIngredientFormSet
from django.db.models import Q, Sum
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Dish, Ingredient, Order, DishIngredient, OrderIngredient
from rest_framework.authtoken.models import Token


class NoCookPermissionView(TemplateView):
    template_name = "foodprod/no_cook_permission.html"


class NoAdminPermissionView(TemplateView):
    template_name = "foodprod/no_admin_permission.html"


class IndexView(ListView):
    template_name = "foodprod/index.html"
    model = Dish

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        token = None
        if self.request.user.is_authenticated:
            token, created = Token.objects.get_or_create(user=self.request.user)
        context.update(token=token)
        return context

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


class DishCreateView(UserPassesTestMixin, CreateView):
    model = Dish
    fields = ['name', 'description']
    success_url = reverse_lazy('foodprod:index')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('foodprod:no_cook_permission')

    def get_context_data(self, **kwargs):
        context = super(DishCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['dish_ingredient_formset'] = DishIngredientFormSet(self.request.POST)
        else:
            context['dish_ingredient_formset'] = DishIngredientFormSet()
        return context

    def form_valid(self, form):
        dish = form.save(commit=False)
        dish.author = self.request.user
        dish.save()
        context = self.get_context_data(form=form)
        formset = context['dish_ingredient_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)


class DishUpdateView(UserPassesTestMixin, UpdateView):
    model = Dish
    fields = ['name', 'description']
    success_url = reverse_lazy('foodprod:index')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('foodprod:no_cook_permission')

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
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)


class DishDeleteView(UserPassesTestMixin, DeleteView):
    model = Dish
    success_url = reverse_lazy('foodprod:index')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('foodprod:no_cook_permission')


class IngredientsListView(ListView):
    template_name = "foodprod/ingredients.html"
    model = Ingredient


class IngredientDetailView(DetailView):
    template_name = "foodprod/ingredient.html"
    model = Ingredient


class IngredientCreateView(UserPassesTestMixin, CreateView):
    model = Ingredient
    fields = ['name']
    success_url = reverse_lazy('foodprod:ingredients')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('foodprod:no_cook_permission')

    def form_valid(self, form):
        ingredient = form.save(commit=False)
        ingredient.author = self.request.user
        ingredient.save()
        return super().form_valid(form)


class IngredientUpdateView(UserPassesTestMixin, UpdateView):
    model = Ingredient
    fields = ['name']
    success_url = reverse_lazy('foodprod:ingredients')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('foodprod:no_cook_permission')


class IngredientDeleteView(UserPassesTestMixin, DeleteView):
    model = Ingredient
    success_url = reverse_lazy('foodprod:ingredients')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('foodprod:no_cook_permission')


class OrdersListView(ListView):
    template_name = "foodprod/orders.html"
    model = Order


class OrderDetailView(DetailView):
    template_name = "foodprod/order.html"
    model = Order


class OrderCreateView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        dish_id = self.request.POST['dish_id']
        dish = Dish.objects.get(pk=dish_id)
        dish_ingredients = DishIngredient.objects.filter(dish=dish)
        quantity_sum = dish_ingredients.aggregate(Sum('quantity')).get('quantity__sum', 0.0)
        if dish_ingredients and quantity_sum > 0:
            order = Order.objects.create(author=request.user)
            for obj in dish_ingredients:
                OrderIngredient.objects.create(order=order, ingredient=obj.ingredient, quantity=obj.quantity)
            return redirect('foodprod:order_update', pk=order.pk)
        else:
            return redirect('foodprod:index')


class OrderUpdateView(UserPassesTestMixin, UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('foodprod:orders')

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('foodprod:no_admin_permission')

    def get_context_data(self, **kwargs):
        context = super(OrderUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['order_ingredient_formset'] = OrderIngredientFormSet(self.request.POST, instance=self.object)
            context['order_ingredient_formset'].full_clean()
        else:
            context['order_ingredient_formset'] = OrderIngredientFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['order_ingredient_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)


class OrderDeleteView(UserPassesTestMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('foodprod:orders')

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('foodprod:no_admin_permission')
