from django.urls import path
from . import views

app_name="book"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('create/', views.create, name="create"),
]