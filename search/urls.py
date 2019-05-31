
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
#from users import views as user_views
from snoop import views
from django.contrib.auth import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('snoop.urls')),
    #url(r'^settings/$', core_views.settings, name='settings'),
    #url(r'^settings/password/$', core_views.password, name='password'),
]
