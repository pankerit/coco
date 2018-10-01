from django.urls import path, include
from . import views, api




urlpatterns = [
    path('', views.home, name='home'),
    path('catalog', views.catalog, name='catalog'),
    # path('detail', views.product, name='product-detail'),
    path('detail/<slug:slug>/', views.product, name='detail'),
    path('cart', views.cart, name='cart'),
    path('post_cart', api.post_cart, name='post_cart'),
    path('post_cart_remove', api.post_cart_remove, name='post_cart_remove'),
    
    
    
    #path('<slug:slug>/', views.smartphone, name='smartphone')

    #path((<>), views.smartphone, name='smartphone'),
]