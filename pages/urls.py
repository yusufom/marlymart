from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='Home'),
	path('merchants/', views.vendors_list, name='Vendors'),
	path('merchants/<int:pk>/<str:pk_test>/', views.vendors_view, name='VendorsView'),
	path('about/', views.about_us, name='AboutUs'),
	path('contact/', views.Contact, name='Contact'),
	path('shop/', views.shop, name='Shop'),
	path('search/', views.search, name='Search'),
	path('search_auto/', views.search_auto, name='search_auto'),
	path('shop/<str:pk_test>/', views.ProductView, name='ProductView'),
	path('category/<int:id>/<slug:slug>/', views.CategoryView, name='CategoryView'),
	path('shop/products/<int:pk_test>/<str:pk_live>/', views.ProductView, name='ProductView'),
]
