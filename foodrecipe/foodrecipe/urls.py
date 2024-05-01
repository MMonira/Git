
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signinpage,name='signin'),
    path('signup/',signuppage,name='signup'),
    path('logoutt/',logoutpage,name='logoutt'),
    path('dashboard/',dashboardpage,name='dashboard'),
    path('profile/',profilepage,name='profile'),
    path('viewrecipe/',viewrecipepage,name='viewrecipe'),
    path('addrecipe/',addrecipepage,name='addrecipe'),
    path('update/',updaterecipe,name='update'),
    path('editrecipe/<str:myid>',editrecipepage,name='editrecipe'),
    path('deletee/<str:myid>',deleterecipe,name='delete'),
    path('viewe/<str:myid>',viiew,name='view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
