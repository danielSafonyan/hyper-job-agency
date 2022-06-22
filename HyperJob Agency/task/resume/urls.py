from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyResumeView.as_view()),
]
