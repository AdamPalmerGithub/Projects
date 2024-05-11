class car:
    colour = "red"

    def start(self):
        print ("car has started")



class car:
    __engineSize = 2000 #private   underscores 2 = private
    _milage = 0 #protected


    def __start_engine(self):
        self._milage += 10
        print("engine has started")

#example 1
class Person:     #private changed to protected
    _name = "John"

    def _greet(self):
        print("Hello, my name is ", self._name)

p1 = Person()
p1._name()
p1._greet()