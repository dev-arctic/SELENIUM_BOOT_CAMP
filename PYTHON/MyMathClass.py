# Self'i anlamak.
class myMath: # Parametrelerim self'den sonra basliyor.
            # Contructor in python burada init. # super = onun base class'i Math'in
    # sayi1 = 0, self.sayi ile bu ayni 
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1 # Self ile init in icinde everensel degiskenler tutua bilirim.
        self.sayi2 = sayi2

    def topla(self):# python bizim matematik classi ile ilgili bir sey yariz diye korkuyor o yuzden zorluyor yazmamizi oop kyonudnen bir tik zayifmis,
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2

matematik = myMath(sayi1= 1,sayi2= 2) # () = yapici blok constructor
# print(matematik.topla())


# inheritance
class Istatistik(myMath):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)


a = Istatistik(1,3)

print(a.topla())