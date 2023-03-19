import UserModel
import Employee
import Customer

class empDB(UserModel.UserModels):
    emp1 = Employee.Employees(
        firstName='Kathlen',
        lastName='Cameron',
        status= Employee.Status.generalManager.value,
        phoneNumber='(206) 342-8631',
        adress= 'Street: 3573 Skips Lane City: Phoenix State/province/area: AZ(Arizona), Zip code > 85012, Country calling code + 1, Country > United States',
        wage= Employee.Wage.generalManager.value
    )
    emp2 = Employee.Employees(
        firstName='larry',
        lastName='Fink',
        status= Employee.Status.networkAdmin.value,
        phoneNumber='(717) 550-1675',
        adress= '3014 R Street Northwest, Washington AR ',
        wage= Employee.Wage.networkAdmin.value
    )
    emp3 = Employee.Employees(
        firstName='Kayla',
        lastName='Edvards',
        status= Employee.Status.salesManager.value,
        phoneNumber='(707)-515-5279',
        adress= '1125 West 41st Street, Savannah GA 31415',
        wage= Employee.Wage.salesManager.value
    )
    emp4 = Employee.Employees(
        firstName='Jose',
        lastName='Simmons',
        status= Employee.Status.cleaningTeam.value,
        phoneNumber='(702)-213-1548',
        adress= '13417 West Marlette Court, Litchfield Park AZ 85340',
        wage= Employee.Wage.cleaninTM.value

    )
   

    employee = [emp1,emp2,emp3,emp4]


        
class customerDB:
    customer = []