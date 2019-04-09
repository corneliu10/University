-- TEMA 1 - Corneliu Dumitru
/*
-- I
1.A
2.A
3.C
4.C
5.09-MAR-09
6.D
*/

-- II
-- 1
select cust_id Cod, cust_name Name
from customer_tbl
where cust_state in ('IN', 'OH', 'MI', 'IL')
and lower(cust_name) like 'a%' or lower(cust_name) like 'b%'
order by cust_name;

-- 2
-- a
select prod_id Cod, prod_desc Descriere, cost Cost
from products_tbl
where cost between 1 and 12.50;

--b
select prod_id Cod, prod_desc Descriere, cost Cost
from products_tbl
where cost < 1 or cost > 12.50;

-- 3
select lower(first_name)||'.'||lower(last_name)||'@ittech.com' from employee_tbl;

-- 4
select first_name||', '||last_name Name, 
       substr(emp_id, 0, 3)||'-'||substr(emp_id, 4, 2)||'-'||substr(emp_id, 6, 4),
       '('||substr(phone, 0, 3)||')'||substr(phone, 4, 3)||'-'||substr(phone, 7, 4)
from employee_tbl;

-- 5
select emp_id Cod, to_char(date_hire, 'YYYY') "Anul angajarii"
from employee_pay_tbl;

-- 6
select e.emp_id Cod, e.last_name Nume, e.first_name Prenume, ep.salary Salariu, ep.bonus Bonus
from employee_tbl e
inner join employee_pay_tbl ep on e.emp_id = ep.emp_id;

-- 7
select c.cust_name "Nume client", o.ord_num "Cod comanda", o.ord_date "Data lansarii"
from customer_tbl c
inner join orders_tbl o on o.cust_id = c.cust_id
where upper(c.cust_state) like 'I%'; 

-- 8
select o.ord_num "Numar comanda", o.qty Cantitate, e.last_name Nume, e.first_name Prenume, e.city Oras
from employee_tbl e
inner join orders_tbl o on e.emp_id = o.sales_rep;

-- 9
select o.ord_num "Numar comanda", o.qty Cantitate, e.last_name Nume, e.first_name Prenume, e.city Oras
from employee_tbl e
left join orders_tbl o on e.emp_id = o.sales_rep;

-- 10
select emp_id, first_name, last_name 
from employee_tbl
where middle_name is NULL;

-- 11
select 
    e.first_name Prenume, 
    e.last_name Nume, 
    nvl(ep.salary, 0) * nvl(ep.pay_rate, 1) + nvl(ep.bonus, 0) "Salariu Anual"
from employee_tbl e
inner join employee_pay_tbl ep on e.emp_id=ep.emp_id;

-- 12
-- met 1
select 
    e.first_name||' '||e.last_name Nume, 
    nvl(ep.salary, 0) Salariu, 
    ep.position Pozitie,
    case lower(ep.position)
        when 'marketing' then ep.Salary * 110/100
        when 'salesman' then ep.Salary * 115/100
        else nvl(ep.Salary, 0)
    end "Salariu modificat"
from employee_tbl e
inner join employee_pay_tbl ep on ep.emp_id=e.emp_id;

-- met 2
select 
    e.first_name||' '||e.last_name Nume, 
    nvl(ep.salary, 0) Salariu, 
    ep.position Pozitie,
    decode(lower(ep.position), 'marketing', ep.salary * 110/100, 'salesman', ep.salary * 115/100, nvl(ep.salary, 0)) "Salariu modificat"
from employee_tbl e
inner join employee_pay_tbl ep on ep.emp_id=e.emp_id;
