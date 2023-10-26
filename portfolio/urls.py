from django.urls import path
from . import views

# creating paths here
urlpatterns =[
    path('', views.home)
]