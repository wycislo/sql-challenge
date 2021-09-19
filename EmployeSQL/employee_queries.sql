-- list employee, number, last name, first name, sex, salary 

select * from employees;

select * from salaries

-- 1. list employee, number, last name, first name, sex, salary 
select e.emp_no, e.last_name, e.first_name, e.sex,salaries.salary from employees e
join salaries on e.emp_no = salaries.emp_no;

-- 2. List first name, last name, and hire date for employees who were hired in 1986.
select e.first_name,e.last_name,e.hire_date
from employees e
where date_part('year',e.hire_date) = 1986

-- 3. List the manager of each department with the following information: department number, 
-- department name, the manager's employee number, last name, first name.

select dept_manager.dept_no, departments.dept_name, employees.emp_no, employees.last_name, employees.first_name
from employees
inner join dept_manager on dept_manager.emp_no = employees.emp_no
inner join departments on departments.dept_no = dept_manager.dept_no

-- 4. List the department of each employee with the following information: employee number, last name, first name, and department name.
select E.emp_no,E.last_name,E.first_name,D.dept_name 
from employees E
join dept_emp DE on E.emp_no = DE.emp_no
join departments D on D.dept_no = DE.dept_no

-- 5. List first name, last name, and sex for employees whose first name is "Hercules" 
-- and last names begin with "B."

select e.first_name, e.last_name, e.sex
from employees e
where e.first_name = 'Hercules' and e.last_name like 'B%'

-- 6. List all employees in the Sales department, including their employee number, 
-- last name, first name, and department name.

select * from departments;
-- old school 
select employees.first_name, employees.last_name, employees.emp_no, departments.dept_name
from employees, departments, dept_emp
where employees.emp_no = dept_emp.emp_no
and dept_emp.dept_no = departments.dept_no
and dept_name = 'Sales'
-- ansi sql 
select employees.first_name, employees.last_name, employees.emp_no, departments.dept_name
from employees
join dept_emp on employees.emp_no = dept_emp.emp_no
join departments on departments.dept_no = dept_emp.dept_no
where dept_name = 'Sales'

-- 7. List all employees in the Sales and Development departments, including their 
-- employee number, last name, first name, and department name.

select employees.first_name, employees.last_name, employees.emp_no, departments.dept_name
from employees
join dept_emp on employees.emp_no = dept_emp.emp_no
join departments on departments.dept_no = dept_emp.dept_no
where dept_name in ('Sales','Development')


-- 8. In descending order, list the frequency count of employee last names, i.e., 
-- how many employees share each last name.

select count(*) ,last_name
from employees
group by last_name
order by 1 desc



