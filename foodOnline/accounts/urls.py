from django.urls import path,include
from . import views
urlpatterns = [
    path('registerUser/', views.registerUser,name='registerUser'),
  
    
]