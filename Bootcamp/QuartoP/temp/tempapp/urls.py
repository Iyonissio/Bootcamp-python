from django.urls import path
from . import views


app_name = 'tempapp'

urlpatterns = [
    path('other/', views.other),
]


