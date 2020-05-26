class area:
    def __init__(self,length,breadth,radius):
        self.length = length
        self.breadth = breadth
        self.radius = radius
    def sqaure(self):
        print(self.length*self.length)
    def circle(self):
        print(self.radius*self.radius * 3.14 )
    def rectangle(self):
        print(self.length*self.breadth)
