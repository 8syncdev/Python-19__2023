        -- self.cccd = cccd
        -- self.full_name = full_name
        -- self.email = email
        -- self.password = password
        -- # Tài khoản mặc định là chưa được chấp nhận
        -- # active: kích hoạt tài khoản
        -- self.active = False
        -- # quyền : user là admin hay là user
        -- self.role = 'user'


-- CREATE TABLE User (
--     _user_id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 1,
--     cccd TEXT NOT NULL UNIQUE,
--     full_name TEXT NOT NULL,
--     password TEXT NOT NULL
-- );

-- UNIQUE: tồn tại duy nhất
-- Constraint: ràn buộc.

-- INSERT INTO User (cccd, full_name, password)
-- VALUES ('121212', 'Nguyen Van A', 'dsfdssssf');

SELECT *
FROM User
WHERE cccd > 150000
ORDER BY cccd DESC