from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUSerForm
# from .decorators import unauthenticated_user, users_allowed, admin_only
from django.core.mail import send_mail
from django.http import HttpResponse
from accounts.models import Customer, Category
from pages.models import HomeSetting
# Create your views here.


# @unauthenticated_user
def registerPage(request):
	category 			=	Category.objects.all()
	Home 				=	HomeSetting.objects.get(id=1)	
	form 				=	CreateUSerForm()
	if request.method 	== 'POST':
		form 			=	CreateUSerForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			customer 	=	Customer()
			customer.user =	user
			user.customer.first_name = form.cleaned_data.get('first_name')
			user.customer.last_name = form.cleaned_data.get('last_name')
			user.customer.email = form.cleaned_data.get('email')
			user.customer.business_name = form.cleaned_data.get('business_name')
			user.customer.save()
			#form 		=	CreateUSerForm()
			username 	=	form.cleaned_data.get('username')
			
			messages.success(request, 'Account successfully created for ' +  username)
			return redirect('Login')
	context				=	{
							'form': form,
							'category': category,
							'Home': Home,
			}
	return render(request, 'register.html', context)

# @unauthenticated_user
def loginPage(request):
	category 			=	Category.objects.all()
	Home 				=	HomeSetting.objects.get(id=1)
	if request.method 	== 'POST':
		username		=	request.POST.get('username')
		password		=	request.POST.get('password')
		user 			=	authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Userpage', id('pk'))
			# return render(request, 'profilepage.html')
		else:
			messages.info(request, 'Username or Password is incorrect, Try again')
	context	=	{
					'category': category,
					'Home': Home,
	}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('Login')


@login_required(login_url = 'Login')
def profilePageUser(request, pk):
	Home 				=	HomeSetting.objects.get(id=1)
	category    		=   Category.objects.all()
	pk					=	request.user.id
	customers  			=	Customer.objects.get(id=pk)
	order      			=   customers.order_set.all().order_by('-id')[:5][::-1]
	orders      		=   customers.order_set.all()
	order_count 		=	orders.count()
	order_cancel		=	customers.order_set.filter(status='Cancelled').count()
	order_pending		=	customers.order_set.filter(status='Pending').count()
	order_OFD			=	customers.order_set.filter(status='Out for delivery').count()
	order_delivered		=	customers.order_set.filter(status='Delivered').count()
	customer 			=	Customer.objects.all()
	context				=	{
							'customer': customer,
							'customers': customers,
							'category': category,
							'order': order,
							'orders': orders,
							'order_cancel': order_cancel,
							'order_count': order_count,
							'order_pending': order_pending,
							'order_OFD': order_OFD,
							'order_delivered': order_delivered,
							'Home': Home,
							}
	return render(request, 'profile.html', context)