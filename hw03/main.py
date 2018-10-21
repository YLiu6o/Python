class Rectangle(object):
    def __init__(self, width, height):
        self.width =width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):

    def __init__(self, width):
        self.width  = width
        self.height = width



class Circle(object):
    def __init__(self, radius):
        self.width =radius

    def area(self):
        return (3.14*self.width)/2


class Ellipse(Rectangle):
    def area(self):
        return 3.14*(self.width/2)*(self.height/2)

    

def compute_area(shapes):
    return sum(x.area()for x in shapes)


