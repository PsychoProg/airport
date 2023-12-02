from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home_view),    
    path('about/', views.about_view),    
    path('reserve/', views.reserve_view),    
    path('deals/', views.deals_view),    
]