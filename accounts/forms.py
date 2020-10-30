from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import Product, Customer, Order


class ProductsForm(forms.ModelForm):
	"""docstring for CreateUSerForm"""
	product_pic			=	forms.ImageField()
	title				=	forms.CharField(widget = forms.TextInput(attrs	=	{
										"placeholder"	:'Title',
										"class"			: 'products',
										"id"			: 'products',
										}))
	description			=	forms.CharField(widget = forms.Textarea(attrs	=	{
										"placeholder"	:'Description',
										"class"			: 'products1',
										"id"			: 'products1',
										}))
	price				=	forms.DecimalField(widget = forms.NumberInput(attrs	=	{
										"placeholder"	:'0.00',
										"class" 		: 'products',
										 "placeholder"	:'₦',
										 "id" 		: 'products',
										 }))

	class Meta:
		model 		=	Product
		fields		=	('product_pic', 'title', 'description', 'availability','price', 'category')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude=	['user']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class CreateOrderForm(forms.ModelForm):
	product 	=	forms.CharField(max_length=200)
	class Meta:
		model 	=	Order
		fields	=	('name_of_customer', 'product', 'status',)