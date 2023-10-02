-- Đọc dữ liệu trong bảng ghi
-- *: lấy tất cả các cột trong bảng




-- SELECT * FROM pets;


-- Lấy cột mà muốn sử dụng:

-- SELECT name FROM pets;


-- Chỉnh sửa dữ liệu:

-- UPDATE tên_table
-- SET cột = giá_trị_mới
-- WHERE điều_kiện

-- UPDATE pets
-- SET weight = 50
-- WHERE _id = 2;

-- SELECT weight FROM pets WHERE _id = 2;


-- Xóa record/tuple(hàng)

DELETE FROM pets WHERE gender = 1 AND weight < 6;

SELECT * FROM pets;