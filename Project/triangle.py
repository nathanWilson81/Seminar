import math
import pytest


class Triangle:
    def __init__(self, name):
        self.name = name
        self.xLen = 0
        self.yLen = 0
        self.zLen = 0
        self.xAngle = 0
        self.yAngle = 0
        self.zAngle = 0
        self.perimeter = 0
        print(self.name)

    def findZLen(self):
        print("I got called")
        self.zLen = math.sqrt((self.xLen**2) + (self.yLen**2) - (2 *
                                                                 self.xLen * self.yLen * math.cos(self.yAngle)))  # Law of cosines
        return self.zLen

    def findPerimeter(self):
        self.findZLen()
        self.perimeter = self.xLen + self.yLen + self.zLen
        return self.perimeter

    def findZAngle(self):
        self.ZAngle = math.asin(
            (math.sin(math.degrees(self.yAngle)) * self.xLen) / self.zLen)  # Law of Sines
        return math.degrees(self.ZAngle)

    def findArea(self):
        # Heron's Formula
        return math.sqrt(self.perimeter * (self.perimeter - self.xLen) * (self.perimeter - self.yLen) * (self.perimeter - self.zLen))


def main():
    t = Triangle('Test Triangle')
    t.xLen = 85
    t.yLen = 90
    t.yAngle = 110
    print("Length of the Z side is: " + str(t.findZLen()))
    print("Perimeter of the triangle is: " + str(t.findPerimeter()))
    print("Z Angle is: " + str(t.findZAngle()))
    print("Area of the triangle is: " + str(t.findArea()))
    print("Ratio of perimeter to area is: " +
          str(t.findPerimeter() / t.findArea()))


def test_Triangle():
    t = Triangle('Test')
    t.xLen = 85
    t.yLen = 90
    t.yAngle = 110
    assert abs(t.findPerimeter() - 349.95719031727197) < .000001
    assert abs(t.findArea() - 64947.92147562526) < .000001

if __name__ == "__main__":
    main()
