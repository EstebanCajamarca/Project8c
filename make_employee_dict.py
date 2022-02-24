# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 2/19/2022

# Write a class named Employee that has private data members for an employee's name, ID_number, salary,
# and email_address. It should have an init method that takes four values and uses them to initialize the data
# members. It should have get methods named get_name, get_ID_number, get_salary, and get_email_address.

# Write a separate function (not part of the Employee class) named make_employee_dict that takes as parameters a list
# of names, a list of ID numbers, a list of salaries and a list of email addresses (which are all the same length).
# The function should take the first value of each list and use them to create an Employee object. It should do the
# same with the second value of each list, etc. to the end of the lists. As it creates these objects, it should add
# them to a dictionary, where the key is the ID number and the value for that key is the whole Employee object. The
# function should return the resulting dictionary. create a class named Employee
import make_employee_dict


class Employee:

    # initialize the attributes
    def __init__(self, name, id_number, salary, email):
        self.__name = name
        self.__id_number = id_number
        self.__salary = salary
        self.__email = email

    # set the attributes
    def set_name(self, name):
        self.__name = name

    def set_id(self, id_number):
        self.__id_number = id_number

    def set_salary(self, salary):
        self.__salary = salary

    def set_title(self, email):
        self.__email = email

    # return the attributes
    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_salary(self):
        return self.__salary

    def get_email(self):
        return self.__email

    # return the objects state as a string


def make_employee_dict(self, emp_names, emp_ids, emp_sals, emp_emails):
    emp_names = get_name(self)

    return make_employee_dict.Employee, make_employee_dict.emp_ids, make_employee_dict.emp_sals, make_employee_dict.emp_emails)



    emp_names = ["Jean", "Kat", "Pomona"]
    emp_ids = ["100", "101", "102"]
    emp_sals = [30, 35, 28]
    emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
    result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
    print(result["100"].get_name())
