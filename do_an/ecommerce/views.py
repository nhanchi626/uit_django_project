from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import User
from .serializers import RegisterSerializer
from .serializers import UserSerializer

# Create your views here.

def member_list(request):
    return HttpResponse("Xin chào mọi người, đây là dự án môn Kĩ thuật lập trình python của nhóm chúng tôi, danh sách thành viên bao gồm : Lê Bùi Khánh Linh, Nguyễn Hoàng Chí Nhân, Tạ Minh An, Phạm Thành Trung")

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class UserDetailView(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(userID=id)
        except User.DoesNotExist:
            return Response({"error": "Người dùng không tồn tại."}, status=404)
        
        serializer = UserSerializer(user)
        return Response(serializer.data)