from django.contrib import admin
from django.urls import path, re_path
from app1_home import views
# from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.welcome,name='welcome'),
    # re_path(r'^$app1_home', include('app1_home')),
]
