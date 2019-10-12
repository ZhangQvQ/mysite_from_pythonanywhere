from django.urls import path
from avgle import views

app_name = "rango"
urlpatterns = [
        path('', views.index, name='index'),
        ]

