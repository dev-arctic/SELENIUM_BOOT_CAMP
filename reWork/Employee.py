import enum
import UserModel
class Employees(UserModel.IUserModel):
    def __init__(self, firstName, lastName, phoneNumber,status, adress,wage):
        self.status = status
        self.wage = wage
        super().__init__(firstName, lastName, phoneNumber, adress)


class Status(enum.Enum):
    generalManager = 'General manager',
    salesManager = 'Sales Manager',
    shippingTeam = 'Shipping Team'
    networkAdmin = 'Network Admin',
    standartEmployee = 'Stanart Employee'
    cleaningTeam = 'Cleaning Team',

class Wage(enum.Enum):
    generalManager = 10.000
    salesManager = 8.500
    shippingTeam = 7.500
    networkAdmin = 7.000
    standartEmp = 5.000
    cleaninTM = 4.000

