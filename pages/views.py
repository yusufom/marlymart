from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import contactForm, SearchForm
from django.conf import settings
from django.contrib import messages
from accounts.models import Product
from django.core.paginator import Paginator
from random import shuffle
from .models import HomeSetting, AboutUs, InstagramPost
from accounts.models import Category, Customer
import json
from .filters import ProductFilter, CustomerFilter
from accounts import models

# Create your views here.
# 
def home(request):
	product 		= 	Product.objects.all()
	product_lists 	= 	Product.objects.all().order_by('?')[:5]
	product_list 	= 	Product.objects.all().order_by('-id')[:5]
	category		=	Category.objects.all()
	# product_cat		=	Product.objects.get(category__in=category.get_descendants(include_self=True))
	# product_cat		=	Product.objects.get(category__pk__in=category.get_descendants(include_self=True).values_list('pk'))
	# product_cat		=	Product.objects.get(category__in=Category.get_queryset_descendants('nodes', include_self=True))
	# node			=	Category.objects.get(title='Electronics')
	# product_cat		=	Category.objects.add_related_count(node.get_children(), Product, 'category', 'product_counts', include_self=True)
	# product_cat 		=	Category.objects.add_related_count(Category.objects.root_nodes(), Product, 'category', 'product_counts', cumulative=True)
	# product_cat		=	products.get_family()
	# product_cat		=	Product.objects.get_queryset_descendants(products, include_self=True)
	insta 			=	InstagramPost.objects.all()
	Home			=	HomeSetting.objects.get(pk=1)
	form 			=	contactForm(request.POST or None)
	if form.is_valid():
		name	=	form.cleaned_data['name']
		subject	=	form.cleaned_data['subject']
		message	=	form.cleaned_data['message']
		email	=	form.cleaned_data['email']
		emailTo		=	[email]
		try:
			send_mail(name, subject, message, email, fail_silently=False)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		form 	=	contactForm(request.POST or None)
		messages.success(request, 'Message successfully sent. Thank you for contacting us')
	context	=	{
					'form' : form, 
					'Home':Home, 
					'category':category, 
					'product_list': product_list,
					'product_lists': product_lists, 
					'insta': insta,
					'product': product,
					# 'product_cat':product_cat,

	}
	return render(request, 'index.html', context)

def vendors_list(request):
	category	=	Category.objects.all()
	Home		=	HomeSetting.objects.get(pk=1)
	customer	=	Customer.objects.all()
	myfilter	=	CustomerFilter(request.GET, queryset=customer)
	customer 	=	myfilter.qs
	insta 		=	InstagramPost.objects.all()
	context		=	{
					'Home':Home, 
					'category':category,
					'customer': customer,
					'insta': insta,
					'myfilter':myfilter,
	}

	return render(request, 'vendors.html', context)

def vendors_view(request, pk, pk_test):
	category	=	Category.objects.all()
	Home		=	HomeSetting.objects.get(pk=1)
	insta 		=	InstagramPost.objects.all()
	customer	=	Customer.objects.get(id=pk)
	customers	=	Customer.objects.filter(business_name=pk_test)
	products     =   customer.product_set.all()
	context		=	{
					'Home':Home, 
					'category':category,
					'customer': customer,
					'customers': customers,
					'products': products,
					'insta': insta,
	}
	return render(request, 'vendors_view.html', context)

def search(request):
	category	=	Category.objects.all()
	Home	=	HomeSetting.objects.get(pk=1)
	if request.method	==	'POST':
		form1	=	SearchForm(request.POST)
		if form1.is_valid():
			query	=	form1.cleaned_data['query']
			catid 	=	form1.cleaned_data['catid']
			if catid	==	0:
				products 	=	Product.objects.filter(title__icontains=query)
			else:
				products 	=	Product.objects.filter(title__icontains=query, category_id=catid)
			categorys 	=	Category.objects.all()
			context		=	{
							'products':products,
							'categorys':categorys,
							'Home': Home,
							'category': category
			}
			return render(request, 'search.html', context)
	return HttpResponseRedirect('/')

def search_auto(request):
	if request.is_ajax():
		q = request.GET.get('term', '')
		products = Product.objects.filter(title__icontains=q)
		results = []
		for rs in products:
			product_json = {}
			product_json = rs.title
			results.append(product_json)
		data = json.dumps(results)
	else:
		data = 'fail'
	mimetype = 'application/json'
	return HttpResponse(data, mimetype)

def CategoryView(request, id, slug):
	Home			=	HomeSetting.objects.get(pk=1)
	category		=	Category.objects.all()
	product 		=	Product.objects.filter(category_id=id)
	myfilter 	=	ProductFilter(request.GET, queryset=product)
	product 	=	myfilter.qs
	context			=	{
					'product':product,
					'category': category,
					'Home': Home,
					'myfilter': myfilter,
	}
	return render(request, 'category_view.html', context)

def ProductView(request, pk_test, pk_live):
	Home	=	HomeSetting.objects.get(pk=1)
	customer	=	Customer.objects.all()
	customers	=	Customer.objects.filter(business_name=pk_test)
	category	=	Category.objects.all()
	product 	=	Product.objects.get(id=pk_test)
	prosim		=	Product.objects.select_related('category')
	products 	=	Product.objects.filter(title=pk_live)	
	context		=	{
					'product':product,
					'category': category,
					'products': products,
					'Home': Home,
					'customer': customer,
					'customers': customers,
					'prosim': prosim,
	}
	return render(request, 'product_view.html', context)

def Contact(request):
	category	=	Category.objects.all()
	Home	=	HomeSetting.objects.get(pk=1)
	form 	=	contactForm(request.POST or None)
	if form.is_valid():
		name	=	form.cleaned_data['name']
		subject	=	form.cleaned_data['subject']
		message	=	form.cleaned_data['message']
		email	=	form.cleaned_data['email']
		# emailTo		=	[settings.EMAIL_HOST_USER]
		message 	=	name  +  ",with the email,"  +  email  +  ",sent the following message:\n\n" + message;
		try:
			send_mail(subject, message, email, ['marlymart2020@gmail.com'],  fail_silently=False)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		messages.success(request, 'Message successfully sent. Thank you for contacting us')
	context	=	{
					'category': category,
					'Home':Home,
					'form':form,
	}
	return render(request, 'contact.html', context)

def about_us(request):
	category	=	Category.objects.all()
	Home		=	HomeSetting.objects.get(pk=1)
	about		=	AboutUs.objects.get(pk=1)
	context		=	{
					'category': category,
					'Home':Home,
					'about': about,
	}
	return render(request, 'AboutUs.html', context)

def shop(request):
	Home	=	HomeSetting.objects.get(pk=1)
	category	=	Category.objects.all()
	customer	=	Customer.objects.all()
	products 	= 	Product.objects.all()
	myfilter 	=	ProductFilter(request.GET, queryset=products)
	products 	=	myfilter.qs
	# product_list	=	list(product)
	# shuffle(product_list)
	# product_lists	=	list(product)
	# shuffle(product_lists)
	# paginator		=	Paginator(product, 4)
	# page_number		=	request.GET.get('page')
	# page_obj		=	paginator.get_page(page_number)
	context			=	{
				'category': category,
				'customer': customer,
				'Home': Home,
				'products': products,
				'myfilter': myfilter
	}
	return render(request, 'shop.html', context)

# def privacy():
	context	=	{}
	return render(request, 'products.html', context)

# def terms_and_agreement():
	context	=	{}
	return render(request, 'products.html', context)