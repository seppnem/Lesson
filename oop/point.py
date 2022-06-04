import math

class Point2D(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        if x < 0:
            x = x * -1
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getDistance(self, point):
        x = self.getX() - point.getX()  # self.__x - gibi de yazılabilir
        y = self.__y - point.getY()

        return math.sqrt(x ** 2 + y ** 2)





#global scope
def main():
    p1 = Point2D(5,5)  #instance object yaratılıyor Point2D
    p2 = Point2D(10,10)

    p1.getDistance(p2)

if __name__ == '__main__':
    main()