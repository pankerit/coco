from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from .models import Shoes, Shoes_size, Shoes_images, Shoes_360, Post_cart
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt

def post_cart(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    shoes_id = data.get("shoes_id")
    size = data.get("size")
    shoes_id = Shoes.objects.filter(shoes_id=shoes_id)[0]
    Post_cart.objects.create(shoes=shoes_id, sessionid=session_key, size=size)
    
    return JsonResponse(return_dict)

def post_cart_remove(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    shoes_id = data.get("shoes_id")
    Post_cart.objects.filter(id=shoes_id).delete()
    print(shoes_id)
    return JsonResponse(dict())