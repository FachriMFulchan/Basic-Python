class A():
    
    def method_A(self):
        print ('ini adalah method A')

class B():
    def method_B(self):
        print ('ini adalah method B')


class C(A, B):
    def __init__(self,name):
        self.name = name


ucup = C('ucup')

ucup.method_A()
ucup.method_B()
print (ucup.name)