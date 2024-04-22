from django.urls import path
from . import views
urlpatterns=[
    path('', views.chat_view, name="chat_view"),
    path('<str:who>/', views.chat_with, name="chat_with"),

]