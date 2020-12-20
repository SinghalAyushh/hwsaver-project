from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
import emailsignup.urls
import favourites.api.urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(emailsignup.urls)),
    path('task2/', include(favourites.api.urls)),
]