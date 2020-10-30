from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from accounts.models import Customer

class CreateUSerForm(UserCreationForm):
	"""docstring for CreateUSerForm"""
	username		=	forms.CharField(widget = forms.TextInput(attrs	=	{
										"class"			: 'form-control',
										"placeholder"	:'Username',
										"id"			: 'InputUsername',
										"value"			: '',}))
	first_name		=	forms.CharField(widget = forms.TextInput(attrs	=	{
										"class"			: 'form-control',
										"placeholder"	:'First Name',
										"id"			: 'InputName',
										"value"			: '',}))
	last_name		=	forms.CharField(widget = forms.TextInput(attrs	=	{
										"class"			: 'form-control',
										"placeholder"	:  'Last Name',
										"id"			: 'InputLastname',
										"value"			: '',}))
	business_name	=	forms.CharField(widget = forms.TextInput(attrs	=	{
										"class"			: 'form-control',
										"placeholder"	: 'Enter Business Name',
										"id"			: 'InputBusinessName',
										"value"			: '',}))
	email			=	forms.CharField(widget = forms.EmailInput(attrs	=	{
										"class"			: 'form-control',
										"placeholder"	:'Enter Email',
										"id"			: 'InputEmail1',
										"value"			: '',}))
	password1		=	forms.CharField(widget = forms.PasswordInput(attrs	=	{
										"class"			: 'form-control',
										"placeholder"	:'Password',
										"id"			: 'InputPassword1',}))
	password2		=	forms.CharField(widget = forms.PasswordInput(attrs	=	{
										"class"			: 'form-control',
										"placeholder"	:'Password Confirmation',
										"id"			: 'InputPassword2',}))
	class Meta:
		model 	=	User
		fields	=	['username',
					'first_name',
					'last_name', 
					'email',
					'business_name', 
					'password1',
					 'password2'
		]