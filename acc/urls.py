from django.urls import path
from . import views

app_name = "acc"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.ulogin, name="login"),
    path('logout/', views.ulogout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('update/', views.update, name="update"),
    path('chpass/', views.chpass, name="chpass"),
    path('delete/', views.delete, name="delete"),
]