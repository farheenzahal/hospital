
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="home"),
    path('about/', views.about,name="about"),
    path('contactus/', views.contactus,name="contactus"),
    path('doctors/', views.doctors,name="doctors"),
    path('departments/', views.departments,name="departments"),
    path('booking/', views.booking,name="booking"),


]  