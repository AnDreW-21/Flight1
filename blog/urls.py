from django.urls import path
import users.views
from . import views
from users import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('about/', views.about, name='blog-about'),
    path('', views.home, name='blog-home'),
    path('booking/', views.booking, name='blog-booking'),

]
