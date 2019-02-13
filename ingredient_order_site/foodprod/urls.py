from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DishDetailView.as_view(), name='dish'),
    path('create/', views.DishCreateView.as_view(), name='dish_create'),
    path('ingredients/', views.IngredientsListView.as_view(), name='ingredients'),
    path('ingredients/<int:pk>/', views.IngredientDetailView.as_view(), name='ingredient'),
    path('ingredients/create/', views.IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredients/update/<int:pk>/', views.IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredients/delete/<int:pk>/', views.IngredientDeleteView.as_view(), name='ingredient_delete'),

]
