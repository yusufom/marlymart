import django_filters
from accounts.models import Product, Customer

class ProductFilter(django_filters.FilterSet):
	class Meta:
		model 	=	Product
		fields 	=	('category', 'availability',)

class CustomerFilter(django_filters.FilterSet):
	class Meta:
		model 	=	Customer
		fields 	=	('business_name', 'state',)