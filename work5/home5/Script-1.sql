CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    created_dt DATE NOT NULL,
    updated_dt DATE NOT NULL,
    order_type TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL,
    serial_no INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES employees (employee_id)
    );
   
CREATE TABLE IF NOT EXISTS employees (
    employee_id SERIAL PRIMARY KEY,
    fio TEXT NOT NULL,
    position TEXT,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)
    ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS departments (
	department_id SERIAL PRIMARY KEY,
	department_name TEXT NOT NULL
	);


DROP TABLE IF EXISTS employees;

INSERT INTO employees VALUES (1, 'Dfcz', '213sdfz', '1');
INSERT INTO departments VALUES (1, 'Dfcz');