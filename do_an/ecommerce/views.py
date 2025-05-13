from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def member_list(request):
    return HttpResponse("Xin chào mọi người, đây là dự án môn Kĩ thuật lập trình python của nhóm chúng tôi, danh sách thành viên bao gồm : Lê Bùi Khánh Linh, Nguyễn Hoàng Chí Nhân, Tạ Minh An, Phạm Thành Trung")
