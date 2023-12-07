from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home_view, name="home"),    
    path('about/', views.about_view, name="about"),    
    path('reserve/<int:flight_id>', views.reserve_view, name="reserve"),    
    path('deals/', views.deals_view, name="deals"),
    path('services/', views.services, name='services'), 
]