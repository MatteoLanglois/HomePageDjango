from . import views
from django.urls import path

app_name = 'accueil'
urlpatterns = [
    path('', views.index, name='Bienvenue !')
]
