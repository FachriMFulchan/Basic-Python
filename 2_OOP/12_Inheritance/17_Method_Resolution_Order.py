'''Multiple Inheritance
Methodnya sama di kedua class, bahkan ketiganya
nah yang bakal ke print yang mana
bisa dilihat di help(objek)
'''

class A():
    def show(self):
        print ('ini adalah method A')


class B():
    def show(self):
        print ('ini adalah method B')


class C(A,B):
    pass


ucup = C()


ucup.show()
print (help(ucup))