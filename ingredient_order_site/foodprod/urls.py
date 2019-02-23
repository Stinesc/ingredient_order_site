from django.urls import path, include, re_path
from . import views
from . import api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('dishes', api_views.DishViewSet)
router.register('ingredients', api_views.IngredientViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
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
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('orders/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('no_cook_permission/', views.NoCookPermissionView.as_view(), name='no_cook_permission'),
    path('no_admin_permission/', views.NoAdminPermissionView.as_view(), name='no_admin_permission'),
]
