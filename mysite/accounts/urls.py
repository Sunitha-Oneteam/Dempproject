
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('accounts/sign_up/',views.sign_up,name="sign-up")
]