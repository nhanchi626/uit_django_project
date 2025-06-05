from django.urls import path
from . import views
from .views import RegisterView
from .views import UserListView
from .views import UserDetailView

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
]

