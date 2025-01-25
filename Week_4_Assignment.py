import mysql.connector

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "empmansys"
        )
        return connection
    except mysql.connector.Error as  err:
        print(f"Error: {err}")
        return None

def Add_Employee(cursor):
    emp_id = int(input("Enter employee ID: "))
    emp_name = input("Enter employee name: ")
    emp_salary = float(input("Enter employee salary: "))
    emp_dept = input("Enter employee department: ")

    query = "Insert into employee values (%s,%s,%s,%s);"
    values = (emp_id,emp_name,emp_salary,emp_dept)
    cursor.execute(query,values)
    print("Employee added successfully!!")

def View_Employee(cursor):
    query = "SELECT * FROM employee;"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for item in results:
            print(f"ID: {item[0]}",end = " ")
            print(f"Name: {item[1]}",end = " ")
            print(f"Salary: {item[2]}",end = " ")
            print(f"Department: {item[3]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def Update_Employee(cursor):
    emp_id = int(input("Enter employee ID of the employee to be updated: "))
    print("Enter what need to be updated?")
    print("1. Name\n2. Salary\n3. Dept")
    ch = int(input("Enter your choice: ")) 
    if ch == 1:
        try:
            new_name = input("Enter new name: ")
            query = "update employee set emp_name = %s where emp_id = %s;"
            values = (new_name,emp_id)
            cursor.execute(query,values)

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
    if ch == 2:
        try:
            new_salary = float(input("Enter new salary: "))
            query = "update employee set emp_salary= %s where emp_id = %s;"
            values = (new_salary,emp_id)
            cursor.execute(query,values)

        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    if ch == 3:
        try:
            new_dept = input("Enter new department: ")
            query = "update employee set emp_dept= %s where emp_id = %s;"
            values = (new_dept,emp_id)
            cursor.execute(query,values)

        except mysql.connector.Error as err:
            print(f"Error: {err}")

def Delete_Employee(cursor):
    try:
        emp_id = int(input("Enter employee ID: "))

        # query = "delete from employee where emp_id= %s;"
        query = f"delete from employee where emp_id like \"{emp_id}%\";"
        cursor.execute(query)
        print("Employee Deleted successfully!!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")



def Search_Employee(cursor):
    try:
        emp_id = int(input("Enter employee ID: "))

        query = "select * from employee where emp_id= %s;"
        values = (emp_id),
        cursor.execute(query,values)
        results = cursor.fetchall()
        for item in results:
            print(f"ID: {item[0]}",end = " ")
            print(f"Name: {item[1]}",end = " ")
            print(f"Salary: {item[2]}",end = " ")
            print(f"Department: {item[3]}")
        

    except mysql.connector.Error as err:
        print(f"Error: {err}")        


def main():  #writing the main function
    connection = connect_to_db()
    if not connection:
        print("failed to connect to database. Exiting...")
        return
    cursor = connection.cursor()
    while(True):
        print("---Employee Management Application---")
        print("1.Add Employee")
        print("2.Update Employee")
        print("3.Delete Employee")
        print("4.View Employee")
        print("5.Search Employee")
        print("6.Exit")
        choice = int(input("enter your choice: "))
        if choice == 1:
            #Add Employee
            Add_Employee(cursor)
        elif choice == 2:
            # Update Employee
            Update_Employee(cursor)
        elif choice == 3:
            #Delete Employee
            Delete_Employee(cursor)
        elif choice == 4:
            #View Employee
            View_Employee(cursor)
        elif choice == 5:
            #Search Employee
            Search_Employee(cursor)
        elif choice == 6:
            #Exit Application
            connection.commit()
            print("Exiting....GoodBye!!..")
            break

if __name__ == "__main__": #standard python code for running the main function first
    main()

