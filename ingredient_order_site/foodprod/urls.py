from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DishDetailView.as_view(), name='dish'),
    path('create/', views.DishCreateView.as_view(), name='dish_create'),
    path('update/<int:pk>/', views.DishUpdateView.as_view(), name='dish_update'),
    path('delete/<int:pk>/', views.DishDeleteView.as_view(), name='dish_delete'),
    path('ingredients/', views.IngredientsListView.as_view(), name='ingredients'),
    path('ingredients/<int:pk>/', views.IngredientDetailView.as_view(), name='ingredient'),
    path('ingredients/create/', views.IngredientCreateView.as_view(), name='ingredient_create'),
    path('ingredients/update/<int:pk>/', views.IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredients/delete/<int:pk>/', views.IngredientDeleteView.as_view(), name='ingredient_delete'),
    path('orders/', views.OrdersListView.as_view(), name='orders'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order'),
    path('orders/create/<int:dish_id>/', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('orders/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
]
