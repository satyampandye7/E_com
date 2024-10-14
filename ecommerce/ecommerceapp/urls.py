from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contect', views.contect, name="contect"),
    path('about', views.about, name="about"),
]






 