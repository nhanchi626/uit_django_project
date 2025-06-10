from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from .views import RegisterView, CustomTokenObtainView
from .views import UserListView
from .views import UserDetailView

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('api/login/', CustomTokenObtainView.as_view(), name='custom_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
]

