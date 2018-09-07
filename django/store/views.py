from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Shoes

# Create your views here.
def home(request):
	
	return render(request, 'home.html')

def shoes(request):
	shoes = Shoes.objects.all()

	return render(request, 'catalog.html', locals())

#def smartphone(request, slug):
#	smartphone = get_object_or_404(Smartphone, slug=slug)
#	context = {
#		'brand': smartphone.brand,
#		'name': smartphone.name,
#	}
#	return render(request, 'ipro/smartphone_detail.html', context)

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