--Laborator 1
--3
desc employees;
desc departments;
desc jobs;
desc locations;
desc job_history;

--4
select * from employees;
select * from departments;
select * from jobs;
select * from job_history;

--5
select employee_id, last_name, job_id, hire_date
from employees;

--6
select employee_id as cod, last_name nume, 
       job_id "Cod job", hire_date "Data angajarii"
from employees;

--7
select job_id "Cod job" from employees;
select unique job_id "Cod job" from employees;

--8
select last_name || ', ' || job_id "Angajat si titlu"
from employees;


--9
--tema

--10
desc employees;
select last_name, salary
from employees
where salary >2850;

--11
select last_name, department_id
from employees
where employee_id=104;

--12
select last_name, salary
from employees
where salary not between 1500 and 2850;

--13
SELECT last_name, job_id,hire_date
FROM employees
WHERE hire_date BETWEEN '20-FEB-1987' and '1-MAY-1989'
ORDER BY 3 desc;