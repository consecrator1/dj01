from django.urls import path
from . import views

app_name="trans"
urlpatterns = [
    path('index/', views.index, name="index"),
    # path('trans/', views.trans, name="trans"),
    # path('change/', views.change, name="change"),
  
]