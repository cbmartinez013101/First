import sqlite3

class Employee:
      def __init__(self, first, last, pay):
             self.first = first
             self.last = last
             self.pay = pay

      def email(self):
              return '{} {}' .format(self.first, self.last)

      def __repr__(self):

              return "Employee('{}, {},{}')".format(self.first, self.last, self.pay)

conn=sqlite3.connect(':memory:')

c=conn.cursor()

c.execute("""CREATE TABLE employees(
            first text,
            last text,
            pay integer
            )""")

def insert_emp(emp):
      with conn:
            c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay':  emp.pay})

def get_emps_by_name(lastname):
      c.execute("SELECT * FROM employees WHERE last=:last",{'last': lastname})
      return c.fetchall()

def update_pay(emp, pay):
      with conn:
            c.execute(""" UPDATE employees SET pay = :pay
                        WHERE first = :first AND last = :last""",
                      {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
      with conn:
            c.execute("DELETE from employees WHERE first = :first AND last = :last",
                      {'first': emp.first, 'last': emp.last})

emp_1=Employee('John', 'Doe', 80000)
emp_2=Employee('Jane', 'Doe', 90000)
emp_3=Employee('Christian', 'Martinez', 150000)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)

emps= get_emps_by_name('Doe')
print(emps)

empl= get_emps_by_name('Martinez')
print(empl)

update_pay(emp_2,95000)

remove_emp(emp_1)

emps= get_emps_by_name('Doe')
print(emps)
conn.close ()

