from django.contrib import admin
from .models import HomeSetting, AboutUs, InstagramPost
# Register your models here.
class HomeSettingAdmin(admin.ModelAdmin):
	"""docstring for 'CustomerAdmin'"""
	list_display	=	['title','keywords','Updated_at',]

class AboutUsAdmin(admin.ModelAdmin):
	"""docstring for 'CustomerAdmin'"""
	list_display	=	['title','name1', 'name2', 'name3', 'name4','Updated_at',]

class InstagramPostAdmin(admin.ModelAdmin):
	"""docstring for 'CustomerAdmin'"""
	list_display	=	['title',]



admin.site.register(HomeSetting, HomeSettingAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(InstagramPost, InstagramPostAdmin)