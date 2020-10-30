from django import forms


class contactForm(forms.Form):
	"""docstring for CreateUSerForm"""
	name			=	forms.CharField(widget = forms.TextInput(attrs	=	{
										"class"			: 'forme2',
										"placeholder"	:'Name',
										"id"			: 'Name',
										}))
	email			=	forms.EmailField(widget = forms.EmailInput(attrs	=	{
										"placeholder"	:'Email',
										"class"			: 'forme2',
										}))
	subject			=	forms.CharField(widget = forms.TextInput(attrs	=	{
										"placeholder"	:'Subject',
										"class"			: 'forme3'}))
	message			=	forms.CharField(widget = forms.Textarea(attrs	=	{
										"placeholder"	:'Message',
										"class" 		: 'forme4',}))

class SearchForm(forms.Form):
	query	=	forms.CharField(max_length=100)
	catid	=	forms.IntegerField()
		