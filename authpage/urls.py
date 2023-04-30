from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('signout',views.signout,name="signout"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    
]