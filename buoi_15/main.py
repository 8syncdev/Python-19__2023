'''
    Cơ sở dữ liệu có cấu trúc:
        - Lưu dữ liệu ở dạng bảng ghi
        - Cột (collumn/field): chứa thông tin của đối tượng
        - Hàng (row/record/tuple): lưu lại tất cả những gì đối tượng truyền vào
        - NOT NULL: cột chứa thông tin không được để trống
        - UNIQUE: dữ liệu đưa vào không được phép trùng nhau
    Tạo cơ sở liệu:
        - Extension: SQLite
        - Tạo file database (kho chứa): 
            - *.db: dấu * đặt tên sao cũng được
        - Viết các query (truy vấn):
            - Create: tạo bảng dữ liệu cho db
            - Insert: thêm dữ liệu cho bảng ghi.
            - Delete: xóa 1 hàng hoặc xóa 1 bảng trong table (chú ý chỉ định rõ ràng)
            - Update: edit lại thông tin (chú ý chỉ định rõ ràng)
            - Dữ liệu xử lý chuỗi:
                - Varchar(số_lượng_kí tự): số kí tự nhỏ vài trăm kí tự
                - Nvarchar(số_lượng_kí tự): số kí tự nhỏ vài trăm kí tự
                    Ví du:
                        nvarchar(50): chỉ cho phép chứa tối đa 50 kí tự
                - Text: số lượng kí tự lớn
                    Ví dụ: bình luận, bài viết,...
'''

