# The Employee class holds data about an employee.

class Employee:

    # The __init__ method is used to initialize the object.

    def __init__(self, name, id_number, department, job_title, salary): # Initializes the object.
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
        self.__salary = salary
    
    def set_name(self, name): # Sets the name of the employee.
        self.__name = name

    def get_name(self): # Returns the name of the employee.
        return self.__name
    
    def set_id_number(self, id_number): # Sets the ID number of the employee.
        self.__id_number = id_number

    def get_id_number(self): # Returns the ID number of the employee.
        return self.__id_number
    
    def set_department(self, department): # Sets the department of the employee.
        self.__department = department

    def get_department(self): # Returns the department of the employee.
        return self.__department
    
    def set_job_title(self, job_title): # Sets the job title of the employee.
        self.__job_title = job_title

    def get_job_title(self): # Returns the job title of the employee.
        return self.__job_title
    
    def set_salary(self, salary): # Sets the new salary of the employee.
        self.__salary = salary

    def get_salary(self): # Returns the new salary of the employee.
        return self.__salary
    
    def increase_salary(self, amount): # Increases the salary of the employee by the amount.
        self.__salary += amount

    def decrease_salary(self, amount): # Decreases the salary of the employee by the amount.
        self.__salary += amount

    def __str__(self): # Returns the string representation of the object.
        return f'Name: {self.__name}\n' + \
               f'ID Number: {self.__id_number}\n' + \
               f'Department: {self.__department}\n' + \
               f'Job Title: {self.__job_title}\n' + \
               f'New Salary: {self.__salary}'