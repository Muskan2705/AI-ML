create database company_db;
USE company_db;
create table EMPLOYEE(
emp_id int,
first_name varchar(50),
last_name varchar(50),
gender char(1),
age int,
department varchar(50),
designation varchar(50),
salary decimal(10,2),
joining_date date,
city varchar(50),
email varchar(50),
phone varchar(15)
);
