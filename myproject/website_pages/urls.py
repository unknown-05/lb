from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('About_us/',views.About_us,name="About_us"),
    path('Contact_us',views.Contact_us,name="Contact_us")
]
