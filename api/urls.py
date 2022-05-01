from django.urls import path
from . import views

urlpatterns = [
    path('',views.getDATA),
    path('addItem/',views.addItem),
]