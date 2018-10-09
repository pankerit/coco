from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Shoes, Shoes_size, Shoes_images, Shoes_360, Post_cart


# Create your views here.
# class ShoesView(viewsets.ReadOnlyModelViewSet)

def home(request):
	
	return render(request, 'home.html')

def catalog(request):
	how_many_shoes_per_page = 42
	# create session key
	if not request.session.session_key:
		request.session.create()
	session_key = request.session.session_key


	all_list = Shoes.objects.all()
	# get shoes type(men, women, kids) lenght
	shoes_men_lenght = len(all_list.filter(shoes_type='men'))
	shoes_women_lenght = len(all_list.filter(shoes_type='women'))
	shoes_kid_lenght = len(all_list.filter(shoes_type='kid'))
	# size_list = Shoes_size.objects.filter(stock=True)

	# filter
	brandFilter = request.GET.get('brand')
	minPrice = request.GET.get('minPrice')
	maxPrice = request.GET.get('maxPrice')
	if (brandFilter or minPrice or maxPrice):
		shoes_list = all_list
		if brandFilter:
			brandFilter = brandFilter.split(',')
			shoes_list = shoes_list.filter(brand__in=brandFilter)
		if (minPrice or maxPrice):
			if not minPrice:
				minPrice = 0
			if not maxPrice:
				maxPrice = 10000
			shoes_list = shoes_list.filter(price__range=(minPrice, maxPrice))
			# cu sablonul nu pot sa pun 2 conditii la jinja si imi arata None daca nu e nimic la price
			if (maxPrice == 10000):
				maxPrice = None
	else: 
		shoes_list = all_list
	# get shoes list lenght
	shoes_list_lenght = len(shoes_list)
	# get all brands
	brands = []
	for a in all_list:
		if not a.brand in brands:
			brands.append(a.brand)
	paginator = Paginator(shoes_list, how_many_shoes_per_page)
	page = request.GET.get('page')
	shoes_list = paginator.get_page(page)
	# get shoes shown lenght
	shoes_list_shown = len(shoes_list)

	# get lenght from cart
	cart = Post_cart.objects.filter(sessionid=session_key)
	cart_lenght = len(cart)
	context = {
		'shoes_list': shoes_list,
		'shoes_list_lenght': shoes_list_lenght,
		'shoes_list_shown': shoes_list_shown,
		'shoes_men_lenght': shoes_men_lenght,
		'shoes_women_lenght': shoes_women_lenght,
		'shoes_kid_lenght': shoes_kid_lenght,
		'brands': brands,
		'brandFilter': brandFilter,
		'minPrice': minPrice,
		'maxPrice': maxPrice,
		'cart_lenght': cart_lenght,
	}
	return render(request, 'catalog.html', context)


# def product(request):
# 	return render(request, 'product-detail.html')

def product(request, slug):
	# unique key
	session_key = request.session.session_key
	# cart lenght
	cart = Post_cart.objects.filter(sessionid=session_key)
	cart_lenght = len(cart)

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
		'img_360': img_360,
		'cart_lenght': cart_lenght,
	}
	return render(request, 'product-detail.html', context)
def cart(request):
	session_key = request.session.session_key
	cart = Post_cart.objects.filter(sessionid=session_key)
	for product in cart:
		shoes_filter = Shoes.objects.filter(post_cart__shoes_id=product.shoes_id)
		product.price = shoes_filter[0].price
		product.slug  = shoes_filter[0].slug
		product.image = shoes_filter[0].image
		product.name = shoes_filter[0].name
		product.brand = shoes_filter[0].brand
	context = {
		'cart': cart,
	}

	return render(request, 'cart.html', context)




















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