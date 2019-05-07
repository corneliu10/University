--- TEMA 3
--- Dumitru Corneliu - grupa 235

--- 1
select s.s_id, s.s_last, 'Student' "Tip"
from student s
join faculty f on (s.f_id = f.f_id)
where lower(f_last) = 'brown'
union
select c.course_no, c.course_name, 'Curs' "Tip"
from course c
join course_section cs on (c.course_no = cs.course_no)
join faculty f on (cs.f_id = f.f_id)
where lower(f.f_last) = 'brown';

--- 2
select s.s_id, s.s_last
from student s
join enrollment e on (s.s_id = e.s_id)
join course_section cs on (e.c_sec_id = cs.c_sec_id)
join course c on (cs.course_no = c.course_no)
where lower(c.course_name) = 'database management'
    and s.s_id not in (
                    select ss.s_id
                    from student ss
                    join enrollment ee on (ss.s_id = ee.s_id)
                    join course_section css on (ee.c_sec_id = css.c_sec_id)
                    join course cc on (css.course_no = cc.course_no)
                    where lower(cc.course_name) = 'programming in c++'
                    );
                    
--- 3
select distinct s.s_id, s.s_last
from student s
join enrollment e on (s.s_id = e.s_id)
where grade is null
    or lower(grade) = 'c';
    
--- 4
select loc_id, bldg_code, capacity
from location
where capacity = (
                 select max(capacity)
                 from location
                 );
                 
--- 5
CREATE TABLE t(id NUMBER PRIMARY KEY);
INSERT INTO t VALUES(1);
INSERT INTO t VALUES(2);
INSERT INTO t VALUES(4);
INSERT INTO t VALUES(6);
INSERT INTO t VALUES(8);
INSERT INTO t VALUES(9);

select min(id) + 1 "Min or max", 'Min' "Tip"
from t
where id + 1 not in (
                    select id
                    from t
                    )
union
select max(id) - 1, 'Maxim'
from t
where id - 1 not in (
                    select id
                    from t
                    );
                    
--- 6
select f.f_id,
    min(f.f_last) || ' ' || min(f.f_first) "Nume",
    decode(count(distinct s.s_id), 0, 'Nu', 'Da (' || count(distinct s.s_id) || ')') "Student",
    decode(count(distinct c.course_no), 0, 'Nu', 'Da (' || count(distinct c.course_no) || ')') "Curs"
from faculty f
left join student s on (f.f_id = s.f_id)
left join course_section cs on (f.f_id = cs.f_id)
join course c on (cs.course_no = c.course_no)
group by f.f_id;

--- 7
select t1.term_id, t1.term_desc, t2.term_id, t2.term_desc
from term t1, term t2
where t1.term_id > t2.term_id
    and substr(t1.term_desc, length(t1.term_desc)) != substr(t2.term_desc, length(t2.term_desc))
    and substr(t1.term_desc, 1, length(t1.term_desc) - 1) = substr(t2.term_desc, 1, length(t2.term_desc) - 1);
    
--- 8
select distinct s.s_id, s.s_last
from student s
join enrollment e1 on (s.s_id = e1.s_id)
join enrollment e2 on (s.s_id = e2.s_id and e1.c_sec_id != e2.c_sec_id)
join course_section cs1 on (e1.c_sec_id = cs1.c_sec_id)
join course_section cs2 on (e2.c_sec_id = cs2.c_sec_id)
where substr(cs1.course_no, 5, 1) != substr(cs2.course_no, 5, 1);

--- 9
select distinct cs1.course_no, cs2.course_no
from course_section cs1, course_section cs2
where cs1.course_no > cs2.course_no
    and cs1.term_id = cs2.term_id;
    
--- 10
select distinct cs.course_no, c.course_name, t.term_desc, cs.max_enrl
from course_section cs
join course c on (cs.course_no = c.course_no)
join term t on (cs.term_id = t.term_id)
where cs.max_enrl < (
                    select min(max_enrl)
                    from course_section
                    where loc_id = 1
                    );

--- 11
select distinct c.course_name, cs.max_enrl
from course c
join course_section cs on (c.course_no = cs.course_no)
where cs.max_enrl = (
                    select min(max_enrl)
                    from course_section
                    );
                    
--- 12
select min(f.f_last), avg(cs.max_enrl)
from faculty f
join course_section cs on (f.f_id = cs.f_id)
group by f.f_id;

--- 13
select min(f.f_last), count(s.s_id)
from faculty f
join student s on (f.f_id = s.f_id)
group by f.f_id
having count(s.s_id) >= 3;

--- 14
select distinct c.course_name, l.capacity, cs1.loc_id
from course c
join course_section cs1 on (c.course_no = cs1.course_no)
join location l on (cs1.loc_id = l.loc_id)
where capacity = (
                  select max(capacity)
                  from location ll
                  join course_section cs2 on (ll.loc_id = cs2.loc_id)
                  where cs1.course_no = cs2.course_no
                  );
                  
--- 15
select t.term_id, min(t.term_desc), avg(cs.max_enrl)
from term t
join course_section cs on (t.term_id = cs.term_id)
where substr(t.term_desc, -4) = '2007'
group by t.term_id;
