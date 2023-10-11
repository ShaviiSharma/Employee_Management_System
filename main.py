from validate import *
class Employee:
    empDict={}
    def __init__(self,emp_id,name,dob,age,gender,phone,email,address,city,salary,pan_card,aadhar,department,designation, maritalstatus ,disability):
        self.emp_id=emp_id
        self.name=name
        self.dob=dob
        self.age=age
        self.gender=gender
        self.phone=phone
        self.email=email
        self.address=address
        self.city=city
        self.salary=salary
        self.pan_card=pan_card
        self.aadhar=aadhar
        self.department=department
        self.designation=designation
        self.maritalstatus=maritalstatus
        self.disability=disability 
        
        if self.department in self.empDict.keys():
            self.empDict[self.department].append(self.name)
        else:
            self.empDict[self.department]=[self.name]

    def display(self):
        print("Employee ID = ", self.emp_id)
        print("employee Name = ", self.name)
        print("Employee age = ", self.age)
        print("Employee Gender = ", self.gender)
        print("Employee phone = ", self.phone)
        print("Employee email = ", self.email)
        print("Employee address = ", self.address)
        print("Employee city = ", self.city)
        print("Employee salary = ", self.salary)
        print("Employee Pan Number = ", self.pan_card)
        print("Employee Aadhaar Number = ", self.aadhar)
        print("Employee department = ", self.department)
        print("Employee designation = ", self.designation)
        print("Employee marital status = ", self.maritalstatus)
        print("Employee disability = ", self.disability)
        
    @classmethod
    def departmentWiseDetails(self):
        for k,v in self.empDict.items():
            print(k," = ",v)
empList=[]
while True:
    print("")
    print("1. Press 1 for adding records")
    print("2. Press 2 for displaying records")
    print("3: Press 3 for searching the employee")
    print("4. Press 4 for the Department wise name of the Employees")
    print("5. Press 5 for deleting the record of the Employee")
    print("6. Press 6 for updating the record of the Employee")
    print("7. Press 7 for maximum salary")
    print("8. Press 8 for minimum salary")
    print("9. Press 9 for exit")
    
    ch=int(input("enter your choice: "))
    
    if ch==1:
        while True:
            emp_id=input("enter the employee id: ")
            if validate_employee_id(emp_id):
                break
            else:
                print("Please enter the correct Employee Id")
        while True:
            name=input("Enter the employee  name : ")
            if validate_name(name):
                break
            else:
                print("Please enter the name correctly")
        while True:
            dob=input("Enter the Date of Birth of the employee: ")
            if validate_dob(dob):
                break
            else:
                print("Enter the correct date of birth.")
        while True:   
            age=input("Enter the age: ")
            if validate_age(age):
                break
            else:
                print("Please enter the correct age")
        while True:    
            gender=input("Enter the gender: ")
            if validate_gender(gender):
                break
            else:
                print("Please enter the correct gender")
        while True:
            phone=input("Enter the employees Phone Number: ")
            if validate_phone_number(phone):
                break
            else:
                print("Enter the correct phone number.")
        while True:
            email=input("Enter the email of employee: ")
            if  validate_email(email):
                break
            else:
                print("Enter the correct email ID.")
        while True:
            address=input("Enter the employee address: ")
            if validate_address(address):
                break
            else:
                print("Please enter the correct address")
        while True:
            city=input("Enter the city: ")
            if validate_city(city):
                break
            else:
                print("Please enter the correct city")
        while True:
            salary=input("Enter the salary: ")
            if validate_salary(salary):
                break
            else:
                print("Please enter the salary correctly")
        while True:
            pan_card=input("Enter the employee Pan Card Number: ")
            if validate_PAN(pan_card):
                break
            else:
                print("Please enter the pan number correctly")
                
        while True:
            aadhar=input("Enter the aadhar card number: ")
            if validate_aadhar(aadhar):
                break
            else:
                print("Please enter the aadhar number correctly")
        while True:
            department=input("Enter the department name: ")
            if validate_department(department):
                break
            else:
                print("Please enter the department name correctly")
        while True:
            designation=input("Enter the employee's designation: ")
            if validate_designation(designation):
                break
            else:
                print("Please enter the designation correctly")
        while True:
            maritalstatus=input("Enter employees Marital Status: ")
            if validate_maritalstatus(maritalstatus):
                break
            else:
                print("Please enter the marital status correctly")
        while True:
            disability = input("Enter disability (yes/no) : ")
            if validate_disability(disability):
                break
            else:
                print("Please enter again if their is any disability")
                
        obj=Employee(emp_id,name,dob,age,gender,phone,email,address,city,salary,pan_card,aadhar,department,designation, maritalstatus, disability )
        empList.append(obj)
        
    elif ch==2:
        for i in empList:
            i.display()
    
    elif ch==3:
        while True:
            print("Press A : To search the Employee by the Employee ID")
            print("Press B : To search the employee by their Name")
            print("Press C : To exit the Searching Window")
            
            ch1=input("Enter the choice: ")
            if ch1=='A':
                p=input("Enter the Employee ID to be searched: ")
                for i in empList:
                    if i.emp_id==p:
                        i.display()
                        
            elif ch1=='B':
                p=input("Enter the name of the Employee to be searched: ")
                for i in empList:
                    if i.name==p:
                        i.display()
                        
            elif ch1=='C':
                break
            
    elif ch==4:
        Employee.departmentWiseDetails()
        
    elif ch==5:
        while True:
            print("Press A : To delete the record by Employee Id")
            print("Press B : To delete the record by Name of the Employee")
            print("Press C : To exit the deletion window")
            
            ch2=input("Enter your Choice")
            if ch2=='A':
                p=input("Enter the Employee ID")
                for i in empList:
                    if i.emp_id==p:
                        empList.remove(i)
                        print("Employee deleted successfully")
        
            elif ch2=='B':
                p=print("Enter the name of the employee")
                for i in empList:
                    if i.name==p:
                        empList.remove(i)
                        print("Employee deleted sucessfully")
                        
            elif ch2=='C':
                break
            
    elif ch==6:
        
        id_update=input("Enter the Employee ID to update the Records: ")
        for i in empList:
            if i.emp_id == id_update:
                print("Current Records:")
                i.display()
                print(" ")
                print("Press 1: To update the name of the Employee")
                print("Press 2: To update the Date of Birth of the Employee")
                print("Press 3: To update the Address of the Employee")
                print("Press 4: To update the Salary of the Employee")
                print("Press 5: To exit the update window")
                
                ch4=int(input("Please choose the details you want to update: "))
                
                if ch4==1:
                    name=input("Name = ")
                    i.name=name
                    print("Name updated Successfully")

                elif ch4==2:   
                    dob=int(input("DOB = "))
                    i.dob=dob
                    print("Date of Birth updated Successfully")
                    
                elif ch4==3:
                    address=input("Address = ")
                    i.address=address
                    print("Address updated Successfully")
                    
                elif ch4==4:
                    salary=int(input("Salary = "))
                    i.salary=salary
                    print("Salary updated Successfully")
                    
                elif ch4==5:
                    break
    
    elif ch==7:
        salaryList=[]
        for i in empList:
            salaryList.append(i.salary)
            
            if len(salaryList)==0:
                print("Please enter records in the list, Employee list is empty")
                print(" ")
            else:
                minSal = min(salaryList)
                print("details of employee with minimum salary : ")
                for i in empList:
                    if i.salary == minSal:
                        i.display()
    
    elif ch==8:
        salaryList=[]
        for i in empList:
            salaryList.append(i.salary)
            
            if len(salaryList)==0:
                print("Please enter records in the list, Employee list is empty")
                print(" ")
            else:
                maxSal = max(salaryList)
                print("Details of the employees with maximum salary: ")
                for i in empList:
                    if i.salary==maxSal:
                        i.display()
        
    elif ch==9:
        print("Exiting the Employee Management System")
        break
    else:
        print("Invalid choice")
    