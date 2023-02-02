from django.urls import path
from . import views

app_name="vote"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('detail/<tpk>', views.detail, name="detail"),
    path('vote/<tpk>', views.vote, name="vote"),
    path('cancel/<tpk>', views.cancel, name="cancel"),
    path('delete/<tpk>', views.delete, name="delete"),
    path('create/', views.create, name="create")
]