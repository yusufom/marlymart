from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProductsForm, ProfileForm, UserForm, CreateOrderForm
from django.contrib import messages
from .models import Product, Customer, Order
from users.forms import CreateUSerForm
from accounts.models import Category
from pages.models import HomeSetting
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'Login')
def upload_products(request, pk):
    Home                =   HomeSetting.objects.get(id=1)
    customers    =  Customer.objects.get(id=pk)
    category    =   Category.objects.all()
    form 	=	ProductsForm(request.POST or None, request.FILES or None)
    if request.method 	== 'POST':
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user.customer;
            obj.save()
            form 			=	ProductsForm()
            messages.success(request, 'Product  has been succesfully uploaded')
    context					=	{
								'form': form,
                                'customers':customers,
                                'category': category,
                                'Home': Home,
				}
    return render(request, 'upload_products.html' , context)

@login_required(login_url = 'Login')
def update_products(request, pk, pk_prod):
    Home                =   HomeSetting.objects.get(id=1)
    customers    =  Customer.objects.get(id=pk)
    category    =   Category.objects.all()
    products    =   Product.objects.get(id=pk_prod)
    form    =   ProductsForm(request.POST or None, request.FILES or None, instance=products)
    if request.method   == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MyProductsView', customers.id)
    context                 =   {
                                'form': form,
                                'customers':customers,
                                'category': category,
                                'products': products,
                                'Home': Home,
                }
    return render(request, 'update_products.html' , context)

@login_required(login_url = 'Login')
def delete_products(request, pk, pk_prod):
    Home                =   HomeSetting.objects.get(id=1)
    customers    =  Customer.objects.get(id=pk)
    category    =   Category.objects.all()
    products    =   Product.objects.get(id=pk_prod)
    if request.method   == 'POST':
        products.delete()
        return redirect('MyProductsView', customers.id)
    context                 =   {
                                'customers':customers,
                                'category': category,
                                'products': products,
                                'Home': Home,
                }
    return render(request, 'delete_product.html' , context)

@login_required(login_url = 'Login')
def update_profile(request, pk):
    Home                =   HomeSetting.objects.get(id=1)
    category    =   Category.objects.all()
    customers    =  Customer.objects.get(id=pk)
    user_form = UserForm(instance=request.user)
    userform = ProfileForm(instance=request.user.customer)
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        userform = ProfileForm(request.POST, request.FILES,instance=request.user.customer)
        if user_form.is_valid() and userform.is_valid():
            user_form.save()
            userform.save()
            user_form = UserForm(instance=request.user)
            userform = ProfileForm(instance=request.user.customer)
            messages.success(request, ('Your profile has been successfully updated!'))
    context      =   {
                'category': category,
                'userform': userform,
                'user_form': user_form,
                'customers':customers,
                'Home': Home,
    }
    return render(request, 'update_profile.html', context)

@login_required(login_url = 'Login')
def orders_view(request, pk):
    Home                =   HomeSetting.objects.get(id=1)
    category    =   Category.objects.all()
    customers    =  Customer.objects.get(id=pk)
    orders      =   customers.order_set.all()
    context     =    {
                    'customers':customers,
                    'category': category,
                    'orders': orders,
                    'Home': Home,
    }
    return render(request, 'orders.html', context)

@login_required(login_url = 'Login')
def update_orders(request, pk, pk_prod):
    Home        =   HomeSetting.objects.get(id=1)
    customers   =  Customer.objects.get(id=pk)
    category    =   Category.objects.all()
    orders      =   Order.objects.get(id=pk_prod)
    form        =   CreateOrderForm(request.POST or None, request.FILES or None, instance=orders)
    if request.method   == 'POST':
        if form.is_valid():
            form.save()
            return redirect('orderView', customers.id)
    context                 =   {
                                'form': form,
                                'customers':customers,
                                'category': category,
                                'Home': Home,
                }
    return render(request, 'update_order.html' , context)

@login_required(login_url = 'Login')
def Myproducts(request, pk):
    Home                =   HomeSetting.objects.get(id=1)
    category    =   Category.objects.all()
    customers    =   Customer.objects.get(id=pk)
    products     =   customers.product_set.all()
    context      =   {
                'products':products,
                'customers':customers,
                'category': category,
                'Home': Home,
    }
    return render(request, 'my_products.html', context)

@login_required(login_url = 'Login')
def CreateOrder(request, pk, pk_prod):
    Home        =   HomeSetting.objects.get(id=1)
    customers   =  Customer.objects.get(id=pk)
    products    =   Product.objects.get(id=pk_prod)
    prod        =   products.title
    category    =   Category.objects.all()
    form        =   CreateOrderForm(request.POST or None, initial={'product': prod})
    if request.method   == 'POST':
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user.customer;
            obj.save()
            form            =   CreateOrderForm()
            return redirect('orderView', customers.id)
            messages.success(request, 'Order has been succesfully created')
    context                 =   {
                                'form': form,
                                'customers':customers,
                                'category': category,
                                'Home': Home,
                }
    return render(request, 'create_order.html' , context)

@login_required(login_url = 'Login')
def userpassword(request, pk):
    customers    =  Customer.objects.get(id=pk)
    if request.method=='POST':
        formie    =   PasswordChangeForm(request.user, request.POST)
        if formie.is_valid():
            user    =   formie.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('UserPassword', customers.id)
        else:
            messages.error(request, 'Please correct the error(s) below. <br>' + str(formie.errors))
            return redirect('UserPassword', customers.id)
    else:
        formie    =   PasswordChangeForm(request.user)
        context =   {
                    'formie': formie,
                    'customers': customers,
        }
        return render(request, 'change_password.html', context)