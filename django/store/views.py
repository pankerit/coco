from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Shoes, Shoes_size, Shoes_images, Shoes_360


# Create your views here.
# class ShoesView(viewsets.ReadOnlyModelViewSet)

def home(request):
	
	return render(request, 'home.html')

def shoes(request):
	# create session key
	if not request.session.session_key:
		request.session.create()
	print(request.session.session_key)
	# create session key
	all_list = Shoes.objects.all()
	size_list = Shoes_size.objects.filter(stock=True)
	try:
		brandFilter = request.GET.get('brand')
		brandFilter = brandFilter.split(',')
		print(brandFilter)
		if brandFilter:
			shoes_list = Shoes.objects.filter(brand__in=brandFilter)
	except: 
		shoes_list = all_list
	
	# get all brands


	brands = []
	for a in all_list:
		if not a.brand in brands:
			brands.append(a.brand)
	paginator = Paginator(shoes_list, 27)
	page = request.GET.get('page')
	shoes_list = paginator.get_page(page)
	context = {
		'shoes_list': shoes_list,
		'brands': brands,
		'brandFilter': brandFilter
	}
	return render(request, 'catalog.html', context)


# def product(request):
# 	return render(request, 'product-detail.html')

def product(request, slug):
	shoes = get_object_or_404(Shoes, slug=slug)
	get_name = shoes.name
	shoes_filter_by_name = Shoes.objects.filter(name=get_name)
	images = Shoes_images.objects.filter(shoes__slug=slug)
	first_image = images[0].image
	size = Shoes_size.objects.filter(shoes__slug=slug).filter(stock=True)
	try:
		img_360 = Shoes_360.objects.filter(shoes__slug=slug)[0].image
	except:
		img_360 = False
	context = {
		'shoes': shoes,
		'size_list': size,
		'shoes_list': shoes_filter_by_name,
		'images': images,
		'first_image': first_image,
		'img_360': img_360
	}
	return render(request, 'product-detail.html', context)




















#def smartphones(request):
#	smartphone = get_object_or_404(Smartphone, slug='samsung-galaxy-s9')
#	images=Image_smartphone.objects.filter(smartphone__slug='samsung-galaxy-s9')
#	context = {
#		'brand': smartphone.brand,
#		'name': smartphone.name,
#		'images': images[0].image.url,
#	}
#	return render(request, 'smartphones.html', context)
# def smartphones(request):
# 	smartphones = Smartphone.objects.all()
# 	return render(request, 'smartphones.html', locals())
# def smartphone(request, slug):
# 	smartphone = get_object_or_404(Smartphone, slug=slug)
# 	images=Image_smartphone.objects.filter(smartphone__slug=slug)
# 	return render(request, 'smartphone.html', locals())

# def headphones(request):
# 	headphones = Headphone.objects.all()
# 	return render(request, 'headphones.html', locals())
# def headphone(request, slug):
# 	headphone = get_object_or_404(Headphone, slug=slug)
# 	images = Image_headphone.objects.filter(headphone__slug=slug)
# 	return render(request, 'headphone.html', locals())


# def laptops(request):
# 	laptops = Laptop.objects.all()
# 	return render(request, 'laptops.html', locals())
# def laptop(request, slug):
# 	laptop = get_object_or_404(Laptop, slug=slug)
# 	images = Image_laptop.objects.filter(laptop__slug=slug)
# 	return render(request, 'laptop.html', locals())