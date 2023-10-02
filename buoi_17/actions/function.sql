CREATE FUNC func_insert_employees(_name TEXT, _salary INTEGER) RETURNS INTEGER 
BEGIN
    INSERT INTO employees (name, salary)
    VALUES (_name, _salary)
    RETURN 1;
END;