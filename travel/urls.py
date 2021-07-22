from django.urls import path
from travel import views

urlpatterns = [
    path('', views.travelHome),
    path('main', views.main, name='main'),
]
