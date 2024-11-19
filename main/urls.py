from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('dop', views.dop, name='dop'),
    path('dop1', views.dop1, name='dop1'),
]