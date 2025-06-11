from itertools import product
from django.http import HttpResponse, Http404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Product, ProductCategory, Role
from .serializers import RegisterSerializer, CustomTokenObtainSerializer, ProductCategorySerializer, UserSerializer, \
    ProductSerializer, RoleSerializer


# Create your views here.
class CustomTokenObtainView(APIView):
    def post(self, request):
        serializer = CustomTokenObtainSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

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

class ProductCategoryListView(APIView):
    def get(self, request):
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductCategoryDetailView(APIView):
    def get(self, request, id):
        try:
            category = ProductCategory.objects.get(categoryID=id)
            serializer = ProductCategorySerializer(category)
            return Response(serializer.data)
        except ProductCategory.DoesNotExist:
            return Response({"error": "Loại sản phẩm không tồn tại."}, status=404)

    def delete(self, request, id):
        try:
            category = ProductCategory.objects.get(categoryID=id)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProductCategory.DoesNotExist:
            return Response({"error": "Loại sản phẩm không tồn tại."}, status=404)

    def put(self, request, id):
        try:
            category = ProductCategory.objects.get(categoryID=id)
        except ProductCategory.DoesNotExist:
            return Response({"error": "Loại sản phẩm không tồn tại."}, status=404)

        serializer = ProductCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductListView(APIView):
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            products = Product.objects.filter(productName__icontains=search_query)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductDetailView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(productID=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Sản phẩm không tồn tại."}, status=404)

    def delete(self, request, id):
        try:
            product = Product.objects.get(productID=id)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Sản phẩm không tồn tại."}, status=404)

    def put(self, request, id):
        try:
            product = Product.objects.get(productID=id)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"error": "Sản phẩm không tồn tại."}, status=404)
        
class RoleListView(APIView):
    def get(self, request):
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response(serializer.data)
    
class RoleDetailView(APIView):
    def get(self, request, id):
        try:
            role = Role.objects.get(roleID=id)
        except Role.DoesNotExist:
            return Response({"error": "Role không tồn tại."}, status=404)
        
        serializer = RoleSerializer(role)
        return Response(serializer.data)
    
class RoleCreateView(APIView):
    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RoleDeleteView(APIView):
    def get_object(self, id):
        try:
            return Role.objects.get(roleID=id)
        except Role.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        role = self.get_object(id)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)