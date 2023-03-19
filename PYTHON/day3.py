# Classes # Modules # Package managment
# allias takma isim vere bilirim
# sadece belli bir bolgeyi import emek icin 
from MyMathClass import myMath as sumFunction
import MyMathClass as matematikFonksiyonlari
from selenium import webdriver
# Disaridan alinan packagelar de import ediliyr buraya

class Human:
    # built-it __init__
    def __init__(self,firstName):
        self.name = firstName # boyle yukraida tanimini vermeden de zaten bir var. olsutumus gibi self.name> yeni variables
        print("A created human instance")
    # ilgili instance geriye donus tipini soyler. direkt kendisini human1 yani 
    def __str__(self):
        return f"STR > {self.name}"
    # def __ diye hazir func. bulariblrim vs.
    def talk(self,sentence): # self demek zorudna degilim ama bir parametre vermek gerkeli mesela Object vs.
        print(f"{self.name} > {sentence}")
        # self.walk()
    def walk(self):
        print(f'{self.name} is walking...')

human1 = Human('Halit')
# human1.name = 'Enes'
human1.talk('Merhaba')
human1.walk()
print(human1)

human2 = Human("Enes")
# human2.name = 'Cem'
human2.talk("Selam")
human2.walk()
print(human2)

calc = matematikFonksiyonlari.myMath(sayi2=2,sayi1=1)
calc2 = sumFunction(sayi2=2,sayi1=2)

print(calc2.topla())

print(calc.cikar())


# Packages > global packages pypi.org 

chromDriver = webdriver.Chrome()