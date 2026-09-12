CREATE DATABASE employee;
USE employee;
CREATE TABLE employee(
EMP_ID INT PRIMARY KEY,
 FIRST_NAME varchar(50),
 LAST_NAME VARCHAR(50),
 GENDER TEXT,
 AGE int,
 DEPARTMENT varchar(50),
 SALARY float,
 JOIN_DATE date,
 EMAIL TEXT,
 PHONE_NO varchar(10),
 CITY varchar(25)
 );
 desc employee;
 INSERT INTO employee: (EMP_ID,FIRST_NAME,LAST_NAME,GENDER,AGE,DEPARTMENT,SALARY,JOIN_DATE,EMAIL,PHONE_NO,CITY)
 VALUES (101,"RAHUL","SHARMA","M",24,"IT",45000,'2024-01-05','rahul@gmail.com','9876543210','Delhi'),
 (102,'Priya','Verma','F',26,'HR',38000,'2023-08-10','priya@gmail.com','9876543211','Noida'),
 (103,'Amit','Singh','M',29,'Finance',55000,'2022-03-20','amit@gmail.com','9876543212','Gurgaon');



alter table employee
add blood_group varchar(10);

alter table employee
add state varchar(50),
add country varchar(50);

alter table employee
modify phone varchar(20);


alter table employee
change designation job_role varchar(40);

alter table employee
drop column blood_group;


create table if not exists employee(
 EMP_ID INT PRIMARY KEY,
 EMP_NAME varchar(50),
 GENDER TEXT,
 AGE int,
 DEPARTMENT varchar(50),
 SALARY float,
 CITY varchar(25),
 EXPERIENCE int
 ); 
 INSERT INTO employee VALUES
(101,'Rahul','M',24,'IT',45000,'Delhi',2),
(102,'Priya','F',26,'HR',38000,'Noida',4),
(103,'Amit','M',30,'Finance',65000,'Delhi',6),
(104,'Neha','F',27,'IT',52000,'Mumbai',5),
(105,'Rohan','M',23,'Sales',32000,'Pune',1),
(106,'Anjali','F',29,'IT',70000,'Delhi',7),
(107,'Mohit','M',31,'HR',42000,'Noida',6),
(108,'Karan','M',25,'Sales',39000,'Delhi',3),
(109,'Sneha','F',28,'Finance',58000,'Mumbai',5),
(110,'Vikas','M',35,'IT',80000,'Gurgaon',10);

select * from employee;

select emp_name from employee;

select emp_name as employee_name from employee;

select distinct department from employee;

select *
from employee
where city = 'delhi';

select *
from employee
where department ='IT';

select *
from employee
where salary > 50000;

select *
from employee
where age <25;

select *
from employee
where salary <= 40000;

select *
from employee
where experience >=5;

select *
from employee
where city!='delhi';

select *
from employee
where salary > 50000 and department = 'IT';

select *
from employee
where city ='delhi' or city = 'Mumbai';

select *
from employee
where not department = 'HR';

select *
from employee order by salary desc;


select *
from employee order by emp_name;

select *
from employee limit 5 ;

select *
from employee order by salary desc limit 3;


select * from employee where age<30;
select * from employee where age>30;

select * from employee where EXPERIENCE>=5;

select * from employee where city ='Delhi' and department = 'IT';

select * from employee where city = 'Delhi' or city = 'mumbai';

select * from employee where city != 'noida';

select distinct department from employee;

select distinct city from employee;

select * from employee order by salary desc; 

select * from employee order by salary asc;

select * from employee order by emp_name; 

select * from employee limit 5 ;

select * from employee order by salary desc limit 3;

select emp_name, department from employee ;




