# Cách cài đặt Jupyter cho VScode

## 1. Cài thư viện môi trường ảo

```
pip install virtualenv
```

## 2. Tạo môi trường ảo

```
py -m venv tên_môi_trường
```

## 3. Kích hoạt môi trường ảo
```
tên_môi_trường/Scripts/activate
```

Tìm từ khóa: Execute Policy of PowerShell

**Cách sửa lỗi**

```
Get-ExecutionPolicy -List
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
tên_môi_trường/Scripts/activate
```

## 4. Các bước sử dụng:
- tạo file jupiter: tên_file.ipynb
- Select kernel: chọn vào môi trường ảo mà các bạn đã tạo.

```
pip install ipykernel -U --force-reinstall
```