from enum import Enum
# Python Variables Types
 
# Metinsel(str) > (String) metinsel ifadeleri belirtmek icin kullanilan bir veri turu 
# mantiksal(bool) > bir problemin soncuunda gore mantiksal bir deger donduren bool mantiksal  beri tipi orengin, bir nullCheck yapacaksiniz bunun icin fonsksiyon yazdin geriye bool donruyor:
# bool isNull(String? ID) {
#       if(ID == null){
#           id = "0" 
#           return false;
#       }else{return true}
#   }
#numerik(int,floatF) > olusturduugmuz degiskenlere saysial degerler vermemizi saglayan veri turleri
# float floatVariables = 1.0F;
# int integerVariables = 1; 
# bence bu duzeyde bunlar yeterli gibi bana.


# kurs icinde sol tarafta odev1, odev2 diye bolumler var bitir dediginide onaylaniyor, onlat iicn dusundum.
def button(click):
    checkBtn = False;
    if click == 1:
        checkBtn = True
        return checkBtn
    else:
        return checkBtn 
    ## tam nalamadim checkBtn bool olsutumadan in not defind diyor returnlere o yuzden boyle yaptim. ney se yavas yavas ogrenicem.
    
if button(1):
    print("Kutucuk onaylandi")
else:
    print("Kutucuk onaylnamadi")


# Ana sayfada ilerleme yuzdesi var mesela bende 90% yine bool kullanilmisola bilir ve 90 = int ola bilir bir algoritma kurup ona gore artirmis ola bilirler. Ornegin;
from enum import Enum

class lessonPercentage(Enum): # enum
    homeWorks = 3.5 # numerik
    videos = 9.0



def percentProgress(getActivity):
    percentage = 0; 
    if getActivity == lessonPercentage.homeWorks:
        percentage = (percentage + lessonPercentage.homeWorks.value)
        print("Ilerlemeniz >",percentage) # tirnak icinde yazilmis metinsel ifade
    if getActivity == lessonPercentage.videos:
        percentage = percentage +  lessonPercentage.videos.value    
        print("Ilerlemeniz >",percentage) # tirnak icinde yazilmis metinsel ifade

## Tabi bu if ile yapilmis spagetti kod umarim bu kamp ile daha iyisini daha OOP  seklinde yaparim

percentProgress(lessonPercentage.videos)