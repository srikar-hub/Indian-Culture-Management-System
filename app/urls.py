from django.urls import *
from .views import *

urlpatterns=[
    path('home',home,name="home"),
    path('signup',signup,name="signup"),
    path('login',login,name="login"),
    path('books',books,name="books"),
    path('festive',festive,name="festive"),
    path('temples',temples,name="temples"),
    path('traditions',traditions,name="traditions"),
    path('adb',adb,name="adb"),
    path('nails',nails,name="nails"),
    path('namaste',namaste,name="namaste"),
    path('am',am,name="am"),
    path('holycow',holycow,name="holycow"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('flipbook',flipbook,name="flipbook"),
]