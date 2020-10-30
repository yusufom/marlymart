from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.shortcuts import reverse
from django.db.models import Q
import operator


User 	=	settings.AUTH_USER_MODEL

# Create your models here.

class Customer(models.Model):
	GENDER				=	(
			('Male', 'Male'),
			('Female', 'Female'),
			('Both', 'Both'),
			)
	STATE				=	(
			('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), 
			('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), 
			('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'),('Edo', 'Edo'), ('Ekiti', 'Ekiti'), 
			('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'),
			('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), 
			('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nassarawa', 'Nassarawa'),('Niger', 'Niger'),  
			('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'),('Plateau', 'Rivers'), 
			('Sokoto', 'Sokoto'),('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara'),
		)
	user 				=	models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	profile_pic			=	models.ImageField(default ='drinkup.jpg', null=True, blank=True)
	business_description=	models.TextField(max_length=200)
	business_name		=	models.CharField(max_length=200)
	phone				=	models.CharField(max_length=200, null=True,)
	whatsapp			=	models.CharField(max_length=200, null=True,)
	gender				=	models.CharField(max_length=10, choices=GENDER)
	state 				=	models.CharField(max_length=50, choices=STATE)
	date_created		=	models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.business_name

class Category(MPTTModel):
	STATUS		=	(
		('True', 'True'),
		('False', 'False'),
		)
	parent		=	TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.SET_NULL)
	title		=	models.CharField(max_length=100)
	keyword		=	models.CharField(max_length=255)	
	description	=	models.TextField(blank=True, null=True)
	status		=	models.CharField(max_length=10, choices=STATUS)
	slug		=	models.SlugField(null=False, unique=True)
	Image		=	models.ImageField(null=True, blank=True,)
	created_at	=	models.DateTimeField(auto_now_add=True, null=True)
	Updated_at	=	models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.title

	class MPTTMeta:
		order_insertion_by	=	['title']

	def get_absolute_url(self):
		return reverse('category_detail', kwargs={'slug': self.slug})

	def __str__(self):
		full_path	=	[self.title]
		k 			=	self.parent
		while k is not None:
			full_path.append(k.title)
			k 	=	k.parent
		return ' / '.join(full_path[::-1])

	def get_queryset_descendants(node, include_self=False):
		if not nodes:
			return Node.tree.none()
		filters	=	[]
		for n in nodes:
			lft, rght	=	n.lft, n.rght
			if include_self:
				lft	-=	1
				rght	+=	1
			filters.append(Q(tree_id=n.tree_id, lft__gt=lft, rght__lt=rght))
		q 	=	reduce(operator.or_, filters)
		return Node.tree.filter(q)

class Product(models.Model):
	AVAILABILITY		=	(
		('On-Order', 'On-Order'),
		('Pre-Order', 'Pre-Order'),
		('Handmade', 'Handmade'),
		('Sold Out', 'Sold Out'),
		)
	user		=	models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
	category 	=	models.ForeignKey(Category, on_delete=models.CASCADE)
	product_pic	=	models.ImageField(null=True, blank=True,)
	title		=	models.CharField(max_length=200)
	description	=	models.TextField(blank=True, null=True)
	price		=	models.DecimalField(decimal_places=2, max_digits=10000)
	availability=	models.CharField(max_length=100, choices=AVAILABILITY)
	created_at	=	models.DateTimeField(auto_now_add=True, null=True)
	Updated_at	=	models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.title

class Order(models.Model):
	STATUS		=	(
		('Cancelled', 'Cancelled'),
		('Pending', 'Pending'),
		('Out for delivery', 'Out for delivery'),
		('Delivered', 'Delivered'),
		)
	user				=	models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
	product 			=	models.CharField(max_length=200, null=True)
	name_of_customer 	=	models.CharField(max_length=100, null=True)
	status				=	models.CharField(max_length=20, choices=STATUS)
	ordered_on			=	models.DateTimeField(auto_now_add=True, null=True)
	Updated_at			=	models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name_of_customer