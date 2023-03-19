faiz = 1.59
vade = "36"
krediAdi = 'Ihtiyac kredisi'
ID = 1
# Type convertion, String to int
print(int(vade) + 12)
faiz = str(faiz)
# dart'daki runTimeType gibi 
print(type(faiz))

# get user input 
# vade = input("istediginiz vade sayisini giriniz > ") 
# Kullanicidan alinan input pythonda varsyilan olarak string olarak aliniyor konsol yapisinda.
print(type(vade))
print(int(vade) / 2)

# buda bir yol, degisimi yaptigin noktanin yeri onemli.
# number = int(input("deger giriniz >"))

print('====' * 6)
# String Interpolation
# formation
print("String interpolation")
print("Sectiginiz vade sonucu ortaya cikan vade > {vadeSayisi}".format(vadeSayisi = vade) )
# 

isim = "halit"
metin = " Merhaba {name}".format(name =  isim)
print(metin)

#  f-string var birde
# {dartdaki giib bunun icine metinin icine kodlari yaza biliyorum}
metin = f"Hosgeldiniz {isim}"

## lists - functions 
print("========" * 6)
print("Lists = Functions")
# listelerde bir veri turuudr.

krediler = ["Ihtiyac kredisi","Tasit kredisi","Konut kredisi"]
print(type(krediler))
print(krediler)
print(len(krediler)) #  listsIndex = length - 1 
dizi = ['Ihtiyac kredisi',10,5.2,True]

krediler.append("Ozel kredi") #dart daki add methodu iste 
krediler.append("X Kredisi")
print(krediler)
krediler.pop(0) # icine deger vermek zorunda degiliz. deleted func. iste varsayilan son elamani siler veririsen istedigini 
print(krediler)

krediler.remove("Tasit kredisi") # buda deger ile hareket ediyor
krediler.append("X Kredisi")
krediler.remove("X Kredisi") # BULDUUGU ILK ELELAMNI SILER

krediler.extend(["y kredisi","z kredisi"]) # birden fazla ekleye biliyorum array gonderiyoruz 


# Loops in pyhton
print("=========="  * 6)
print('Loops in Python')

# Syntax, range icinde aldigi degere kadar ulasatirana kadar calisan bir methid sey gibi i++


# for i in range(3,10):
#     print(i)

# print("===" * 4)
# for i in range(10):
#      print(i)

# for i in range(0,51,10): # sifiirdan basliyor 50 ye kadar 10 ar sekilde artiyor.
#      print(i)


for item in krediler:
     print(item)

print('=============' * 6)

for i in range(len(krediler)):
     print(f"Number > {i,krediler[i]}") # bildigimiz klasik for i degerinin indexine gore aldigimiz.

print("===========" * 6)
j = 0
while(j < 10):
     print(j)
     j += 1

print('=============' * 6)

while True:
     print('hey')
     break # donguyu bitirmis durudurmus oluyor nerde kullanirsan iste
print('=============' * 6)

i = 0
while i<len(krediler):
        
    print(krediler[i])
    i += 1

    if krediler[i] == krediler[2]:
        break

# Function in python
print("=======" * 6)
print('Functions in python')

fiyat = 100
indirim = 20
# define , definition
def calculate(): 
    print(100 - 20)

def calculateWithParams(fiyat,indirim): 
     print(fiyat - indirim)

def sayHello(name):
     print(f"Merhaba {name}")

def calculateAndReturn(price,discount):
     return (price - discount)

calculate()
calculateWithParams(fiyat , indirim)
calculateWithParams(10 , 2)
sayHello("arctic")

yeniFiyat = calculateAndReturn(100,20)
print(yeniFiyat)
