from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('shoes', views.shoes, name='shoes'),
    
    
    
    
    #path('<slug:slug>/', views.smartphone, name='smartphone')

    #path((<>), views.smartphone, name='smartphone'),
]