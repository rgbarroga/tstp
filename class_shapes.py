class Shape:
    def __init__(self, s1, s2=None):
        self.s1 = s1
        self.s2 = s2
            
    def what_am_i(self):
        print('I am a shape')
        
    def calculate_perimeter(self):
        if self.s2 == None:
            return 4*self.s1
        else:
            return 2*(self.s1 + self.s2)

        
class Square(Shape):
    pass

class Rectangle(Shape):
    pass