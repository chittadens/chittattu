from django.urls import URLPattern, path
from .import views
URLPattern =[
    path('1st/',views.display1),
]