# BIR LISTE OALCAK SADECE "AD VE SOYAD " sistem soyle isleyecek al
# #Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.
# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.

users = []

def deleteMultipleUser(getUserID_S = []):
    for i in getUserID_S:
        if i != None:
            users.pop(i)
        else:
            break


def addUser(firstName,lastName):
    result = firstName +" "+lastName
    users.append(result)

def deleteUser(getIndex,user = []):
    result = user[getIndex]
    users.remove(result)

def addMultipleUser(firstNames = [],lastNames = []):
    counter = 0
    result = 0

    while counter <= len(firstNames):  
        if counter < len(firstNames):
            result = firstNames[counter] + " "+lastNames[counter]
            users.extend([result])
            counter += 1
        else:
            break

def printOnScrenUser(user):
    return user
def userNumber(user):
    for i in range(len(user)):
        print(f"Number Of Student > {i,user[i]}")



addUser("kevin","larman")

# deleteUser(0,users)
addMultipleUser(["larry","harry"],['jackson','tedman'])
userNumber(users)
print(printOnScrenUser(users))
print("===========" * 6)
print(len(users))
deleteMultipleUser([2,1,0]) # yani burasi biraz karmasik oldu tersten vermek gerekyoksa index out if rangehatasi aliyorum ve delete user ile cakisiyor onu cozemedim.
print(len(users))