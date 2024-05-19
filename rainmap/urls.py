from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_map, name='show-map'),
    path('api/rainfall-data/', views.get_rainfall_data, name='rainfall-data'),
]