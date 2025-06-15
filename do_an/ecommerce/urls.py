from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views
from .views import RegisterView, CustomTokenObtainView, ProductDetailView, UserListView, UserDetailView, \
    ProductCategoryListView, ProductCategoryDetailView, ProductListView

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('api/login/', CustomTokenObtainView.as_view(), name='custom_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
    path('categories/', ProductCategoryListView.as_view(), name='categories'),
    path('products/', ProductListView.as_view(), name='products'),
    path('categories/<int:id>/', ProductCategoryDetailView.as_view(), name='category'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product'),
]

