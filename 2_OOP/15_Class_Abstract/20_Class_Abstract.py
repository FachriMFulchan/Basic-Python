from abc import ABC, abstractmethod

class Button (ABC):
    
    @abstractmethod
    def click (self):
        print ('button click')


class PushButton (Button):
    def click (self):
        print ('push button click')
    
    def select (self):
        print ('coba')
    

class RadioButton (Button):
    def click (self):
        print ('radio button click')



tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()



'''RADA GANGERTI SIH
INTINYA KALO CLASS ITU ABSTRACT GAAKAN BISA DIBIKIN OBJEK DARI CLASS ITU
JADI KALO DI CLASS ABSRACT ITU ADA METHOD
MAKA HARUS DI EKSEKUSI DI CLASS YANG GEINHERITE NYAA
DAN HARUSSSSSS GABOLEH ENGGA
'''