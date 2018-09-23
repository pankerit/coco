from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('shoes', views.shoes, name='shoes'),
    # path('detail', views.product, name='product-detail'),
    path('detail/<slug:slug>/', views.product, name='detail'),
    
    
    
    
    #path('<slug:slug>/', views.smartphone, name='smartphone')

    #path((<>), views.smartphone, name='smartphone'),
]