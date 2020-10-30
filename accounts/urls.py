from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
	 path('profile/<int:pk>/upload_products/', views.upload_products, name='uploadProducts'),
	 path('profile/<int:pk>/update_products/<int:pk_prod>/', views.update_products, name='updateProducts'),
	 path('profile/<int:pk>/delete_products/<int:pk_prod>/', views.delete_products, name='deleteProducts'),
	 path('profile/<int:pk>/update_profile/', views.update_profile, name='updateProfile'),
	 path('profile/<int:pk>/change_password/', views.userpassword, name='UserPassword'),
	 path('profile/<int:pk>/orders/', views.orders_view, name='orderView'),
	 path('profile/<int:pk>/my_products/', views.Myproducts, name='MyProductsView'),
	 path('profile/<int:pk>/create_order/<int:pk_prod>/', views.CreateOrder, name='CreateOrder'),
	 path('profile/<int:pk>/update_order/<int:pk_prod>/', views.update_orders, name='UpdateOrders'),
]
