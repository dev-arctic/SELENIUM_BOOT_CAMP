class Bank:
    # Self = this, classlarin icinde yaptigim bu def'leri self parametresi vererk kullanmaliyim
    def addUser(self) :
        print("User added")
    def deleteUser(self):
        print("Deleted User")


banka = Bank()
banka.deleteUser()