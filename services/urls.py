from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='services'),
    # path('about/', views.about, name='about'),
    # include('', include('home.urls')),
]
