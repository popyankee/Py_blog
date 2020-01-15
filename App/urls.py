from django.urls import path,include
from App.views import main

urlpatterns = [
    path('', main.index,name='index'),
    path('yankee', main.yankee,name='yankee'),
]
