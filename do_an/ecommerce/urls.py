from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('register/', RegisterView.as_view(), name='register'),
]

