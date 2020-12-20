from django.urls import path, re_path,include
from rest_framework import routers    


from . import views
router = routers.DefaultRouter()  
                     
router.register('', views.FavView, 'todo')  



urlpatterns = [
    path('fav/', include(router.urls)),
  
]


               
               
                          

  
