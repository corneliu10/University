--- TEMA 2
--- Corneliu Dumitru - grupa 235

--- 1
select count(*)
from employees
where upper(last_name) like 'K%';

--- 2
select employee_id, last_name, first_name, salary
from employees
where salary = (select min(salary) from employees);

--- 3
select distinct m.employee_id, m.last_name, m.first_name
from employees e
join employees m on (e.manager_id = m.employee_id)
where e.department_id = 30
order by m.last_name asc;

--- 4
select distinct m.employee_id, m.last_name, m.first_name,
                (select count(*)
                from employees e
                where e.manager_id = m.employee_id)
from employees m
order by 4 desc;      
        
--- 5
select e.employee_id, e.last_name, e.first_name
from employees e
join employees m on (m.last_name = e.last_name)
where m.employee_id <> e.employee_id
order by e.last_name asc;

--- 6
select d.department_id, d.department_name
from departments d
where 1 < (select count(distinct job_title)
            from jobs j, employees e
            where (e.department_id = d.department_id) and
                  (j.job_id = e.job_id))
order by 2 asc;

--- 7
select p.prod_desc, sum(o.qty)
from orders_tbl o
inner join products_tbl p on o.prod_id=p.prod_id
where lower(p.prod_desc) like '%plastic%'
group by p.prod_desc;

--- 8
select last_name, 'angajat' 
from employee_tbl
union all
select cust_name, 'client'
from customer_tbl;

--- 9 
select p.prod_desc
from products_tbl p
join orders_tbl o on(p.prod_id = o.prod_id)
where o.sales_rep in (select ord.sales_rep
                        from orders_tbl ord
                        join (select prod_id
                                from products_tbl
                                where (prod_desc like '_% P% _%') 
                                ) a 
                        on (ord.prod_id = a.prod_id));

--- 10
select c.cust_name, o.ord_date
from customer_tbl c
join orders_tbl o on (o.cust_id = c.cust_id)
where to_char(o.ord_date, 'DD') = 17;

--- 11
select e1.last_name, e1.first_name, e2.salary, e2.bonus
from employee_tbl e1
join employee_pay_tbl e2 on (e1.emp_id = e2.emp_id)
where GREATEST(e2.salary,e2.bonus*17) < 32000;

--- 12
select e.emp_id, e.last_name, sum(nvl(o.qty, 0))
from orders_tbl o
right outer join employee_tbl e on o.sales_rep = e.emp_id
group by e.emp_id, e.last_name
having sum(nvl(o.qty, 0)) > 50 or sum(nvl(o.qty, 0)) = 0;

--- 13
select e.emp_id, e.last_name, e.first_name, e2.salary, max(o.utlimacomanda) as "Ultima Comanda"
from employee_tbl e
join (select a.sales_rep, max(a.ord_date) as utlimaComanda
        from orders_tbl a
        group by a.sales_rep
        having count(prod_id) >= 2) o on e.emp_id = o.sales_rep
join employee_pay_tbl e2 on e2.emp_id = e.emp_id
group by e.emp_id, e.last_name, e.first_name, e2.salary;

--- 14
select prod_id, prod_desc, cost
from products_tbl
where cost > (select avg(cost) from products_tbl);

--- 15
select e.last_name, e.first_name, e2.salary, e2.bonus,
        (select sum(salary)from employee_pay_tbl) as "suma totala",
        (select sum(bonus) "bonusul total" from employee_pay_tbl) as "bonus total"
from employee_tbl e
join employee_pay_tbl e2 on (e.emp_id = e2.emp_id);

--- 16
select e.last_name, e.city from employee_tbl e
where e.emp_id in (select max(count(*))
                    from orders_tbl
                    group by sales_rep);
                    
--- 17 
select distinct e.emp_id, e.last_name, e.first_name,
        decode(extract(month from o.ord_date),
        9,(select count(*)
        from orders_tbl
        where sales_rep = e.emp_id and extract(month from ord_date) = 9),
        10,(select count(*)
        from orders_tbl
        where sales_rep = e.emp_id and extract(month from ord_date) = 10)
        ,0) as NrComenzi,
        decode (extract(month from o.ord_date),
        9, to_char(o.ord_date,'MON'),
        10, to_char(o.ord_date,'MON'),
        0,to_char(o.ord_date,'MON')) as Luna
from employee_tbl e
join orders_tbl o on (e.emp_id = o.sales_rep);

--- 18
select c.cust_name, c.cust_city, c.cust_address
from customer_tbl c
where c.cust_id not in (select cust_id from orders_tbl)
and substr(c.cust_address, 1, 1) in ('0','1','2','3','4','5','6','7','8','9');

--- 19
select e.emp_id, e.last_name, e.city, c.cust_id, c.cust_name, c.cust_city
from employee_tbl e, customer_tbl c, orders_tbl o
where o.cust_id = c.cust_id 
and o.sales_rep = e.emp_id
and e.city <> c.cust_city;

--- 20
select avg(nvl(salary, 0))
from employee_pay_tbl;

--- 21 a) este corecta
SELECT CUST_ID, CUST_NAME
FROM CUSTOMER_TBL
WHERE CUST_ID =
(SELECT CUST_ID
FROM ORDERS_TBL
WHERE ORD_NUM = '16C17');

--- b) nu este corecta, nu exista tabela employee_id
SELECT EMP_ID, SALARY
FROM EMPLOYEE_PAY_TBL
WHERE SALARY BETWEEN '20000'
AND (SELECT SALARY
FROM EMPLOYEE_ID
WHERE SALARY = '40000');

--- 22
select e1.last_name, e2.pay_rate
from employee_tbl e1
join employee_pay_tbl e2 on e1.emp_id = e2.emp_id
where e2.pay_rate > all (select e3.pay_rate
                        from employee_pay_tbl e3
                        join employee_tbl e4 on (e3.emp_id = e4.emp_id)
                        where instr(lower(e4.last_name), 'll') <> 0);
