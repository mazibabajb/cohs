
class CAt:
    name = ''
    age = 0
    color = ''
    

    def __init__(self,name,age=0,color = "white"):
        self.name = name
        self.age = age
        self.color = color
        print(F"consrtuctor of {self.name }")
    
    def meow(self):
        print(f'{self.name}  meow')

    
    def sleep(self):
        print(f'{self.name}  zzzzz')


def test():
    b = CAt('nancy',6,'blue')

    b.sleep()

    print(b)
 
