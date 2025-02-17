from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculate_cost, name='calculate_cost'),
]
