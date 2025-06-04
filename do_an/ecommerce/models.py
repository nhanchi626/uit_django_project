from django.db import models

# Create your models here.
from django.db import models

# 1. Bảng Roles – Vai trò người dùng
class Role(models.Model):
    roleID = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=50)

    def __str__(self):
        return self.roleName

# 2. Bảng Users – Thông tin người dùng
class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userEmail = models.EmailField(unique=True)
    userPassword = models.CharField(max_length=128)
    userFirstName = models.CharField(max_length=50)
    userLastName = models.CharField(max_length=50)
    userPhone = models.CharField(max_length=20)
    userAddress = models.CharField(max_length=255)
    userRoleID = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.userFirstName} {self.userLastName}"

# 3. Bảng ProductCategories – Danh mục sản phẩm
class ProductCategory(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName

# 4. Bảng Products – Sản phẩm
class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productDesc = models.TextField()
    productCategoryID = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    productStock = models.PositiveIntegerField()

    def __str__(self):
        return self.productName

# 5. Bảng Orders – Đơn hàng
class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    orderUserID = models.ForeignKey(User, on_delete=models.CASCADE)
    orderAmount = models.DecimalField(max_digits=12, decimal_places=2)
    orderShipAddress = models.CharField(max_length=255)
    orderPhone = models.CharField(max_length=20)
    orderDate = models.DateTimeField(auto_now_add=True)
    orderShipped = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.orderID} - User {self.orderUserID_id}"

# 6. Bảng OrderDetails – Chi tiết đơn hàng
class OrderDetail(models.Model):
    detailID = models.AutoField(primary_key=True)
    detailOrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    detailProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    detailName = models.CharField(max_length=100)
    detailPrice = models.DecimalField(max_digits=10, decimal_places=2)
    detailQuantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Detail #{self.detailID} - Order #{self.detailOrderID_id}"
