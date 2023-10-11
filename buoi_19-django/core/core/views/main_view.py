from django.shortcuts import render, redirect, HttpResponse

list_product = [
    {
        "id": 1,
        "name": "Iphone 12",
        "price": 3000,
    },
    {
        "id": 2,
        "name": "Iphone 14",
        "price": 6000,
    },
    {
        "id": 3,
        "name": "Iphone 13",
        "price": 5000,
    },
]



so_luong_san_phan = [0] * list_product.__len__() 


def home(request):
    global list_product, so_luong_san_phan
    html = ""
    for item in list_product:
        item_html = f'<p>{item["id"]} {item["name"]} {item["price"]} <a href="http://127.0.0.1:8000/add/?id={item["id"]}">Thêm vào giỏ hàng</a><a href="http://127.0.0.1:8000/sub/?id={item["id"]}">Xóa</a></p>'
        html += item_html
    
    html += f'<h1>Đơn hàng:{sum(so_luong_san_phan)}</h1>'
    return HttpResponse(html)


def about(request):
    return HttpResponse('Hello About Page')


def add(request):
    global so_luong_san_phan
    so_luong_san_phan[int(request.GET.get('id'))-1] += 1
    return redirect('/')

def sub(request):
    global so_luong_san_phan
    if so_luong_san_phan[int(request.GET.get('id'))-1] > 0:
        so_luong_san_phan[int(request.GET.get('id'))-1] -= 1
    return redirect('/')
