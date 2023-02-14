class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        print("self: ",self)
        print("other: ",other)
        if self.x==other.y:
            return True

point=Point(3,5)
print(point)

