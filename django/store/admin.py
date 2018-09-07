from django.contrib import admin
from .models import Shoes

# Register your models here.

# class Shoes_imagesInline(admin.TabularInline):
# 	model = Shoes_images
# 	extra = 0
# class Shoes_360Inline(admin.TabularInline):
# 	model = Shoes_360
# 	extra = 0
# class Shoes_sizeInline(admin.TabularInline):
# 	model = Shoes_size
# 	extra = 0
class ShoesAdmin(admin.ModelAdmin):
	#list_display = [field.name for field in Smartphone._meta.fields] le arate pe toate
	# list_display = [ 'brand', 'name', 'created' ]
	# list_display_links = ['name']
	# inlines = [Shoes_imagesInline, Shoes_360Inline, Shoes_sizeInline]
	# exclude = ['id']
	class Meta:
		model = Shoes

admin.site.register(Shoes, ShoesAdmin)
