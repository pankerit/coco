from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('shoes', views.ShoesView)


urlpatterns = [
    path('', views.home, name='home'),
    path('shoes', views.shoes, name='shoes'),
    path('shoes/api/', include(router.urls))
    
    
    
    
    #path('<slug:slug>/', views.smartphone, name='smartphone')

    #path((<>), views.smartphone, name='smartphone'),
]