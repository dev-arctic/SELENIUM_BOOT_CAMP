import UserDB
import Customer
import Employee
class IUserModel:
    adress = None
    def __init__(self,firstName,lastName,phoneNumber,adress = 'Not Address Added'):
        self.firstName = firstName        
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.adress = adress

    def addNewUser(self,getUser):
        empDB = UserDB.empDB.employee
        customerDB = UserDB.customerDB.customer
        if getUser == Customer.Customer:
            customerDB.append(getUser)
        elif getUser == Employee.Employees:
            empDB.append(getUser)
        else:
            return

    def deleteUser(self,getUser):
        empDB = UserDB.empDB.employee
        customerDB = UserDB.customerDB.customer
        if getUser == Customer.Customer:
            customerDB.remove(getUser)
        elif getUser == Employee.Employees:
            empDB.remove(getUser)
        else:
            return
