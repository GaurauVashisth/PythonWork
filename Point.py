class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        x = self.x
        y = self.y
        z = self.z
        return (x*x + y*y + z*z)
    
newPoint = Point(1,3,5)
print(newPoint.sqSum())
