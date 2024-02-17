# Manny Ozowalu
# Program Status: Complete

import employeeObject

def main(): # Calls the make_list function and prints the list of employees.

    employees = make_list()

    for employee_obj in employees:
        print (employee_obj)
    

def make_list(): # Creates an empty list of employees, gets user input for employee information and returns the list.
    try:

        employee_list = []

        num_employees = int (input ('Please enter the number of employees: '))

        for num in range(num_employees):

            
            print (f'Employee {num + 1}:')

            name = input ('Please enter the employee\'s name: ')
            id_number = int (input ('Please enter the employee\'s ID number: '))
            department = input ('Please enter the employee\'s department: ')
            job_title = input ('Please enter the employee\'s job title: ')
            salary = int (input ('Please enter the employee\'s initial salary: '))

            employee_obj = employeeObject.Employee(name, id_number, department, job_title, salary)
            employee_list.append(employee_obj)

        for employee_obj in employee_list:

            employee_name = employee_obj.get_name()

            amount = int (input (f'Please enter the amount to change {employee_name}\'s salary by (negative if decreased): '))

            if amount > 0:
                employee_obj.increase_salary(amount)

            else:
                employee_obj.decrease_salary(amount)
        
        return employee_list
    
    except ValueError:
        print ('This value must be a number! Please restart the program.')
        exit()

if __name__ == '__main__': # Calls the main function.
    main()