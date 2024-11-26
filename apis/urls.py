from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('make/', RunMigrationsView.as_view(), name='run-migrations'),
    path('dishes/', DishListAPIView.as_view(), name='dish-list'),
    path('dishe/create/', DishCreateAPIView.as_view(), name='dish-create'),
    path('dishe/<int:pk>/', DishRetrieveUpdateAPIView.as_view(), name='dish-detail'),
    path('dishe/<int:pk>/delete/', DishDestroyAPIView.as_view(), name='dish-delete'),

    path('tables/', TableListAPIView.as_view(), name='table-list'),
    path('table/create/', TableCreateAPIView.as_view(), name='table-create'),
    path('table/<int:pk>/', TableRetrieveUpdateAPIView.as_view(), name='table-detail'),
    path('table/<int:pk>/delete/', TableDestroyAPIView.as_view(), name='table-delete'),

    path('bills/', BillListAPIView.as_view(), name='bill-list'),
    path('bill/create/', BillCreateAPIView.as_view(), name='bill-create'),
    path('bill/<int:pk>/', BillRetrieveUpdateAPIView.as_view(), name='bill-detail'),
    path('bill/<int:pk>/delete/', BillDestroyAPIView.as_view(), name='bill-delete'),

    path('orders/', OrderListAPIView.as_view(), name='order-list'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('order/<int:pk>/', OrderRetrieveUpdateAPIView.as_view(), name='order-detail'),
    path('order/<int:pk>/delete/', OrderDestroyAPIView.as_view(), name='order-delete'),
]
