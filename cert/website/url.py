from django.urls import path
from . import views

urlpatterns = [
    path('', cert.views.home, name='home'),
]