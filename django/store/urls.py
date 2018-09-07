from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('shoes', views.shoes, name='shoes'),
    #path('<slug:slug>/', views.smartphone, name='smartphone'),
    # path('smartphones', views.smartphones, name='smartphones'),
    # path('laptops', views.laptops, name='laptops'),
    # path('headphones', views.headphones, name='headphones'),
    # path('smartphones/<slug:slug>/', views.smartphone, name='smartphone'),
    # path('laptops/<slug:slug>/', views.laptop, name='laptop'),
    # path('headphones/<slug:slug>/', views.headphone, name='headphone'),

    #path((<>), views.smartphone, name='smartphone'),
]