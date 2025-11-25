class Rectangle:
    def __init__(self,l,b):
        self._len = l
        self._bre = b

    def getArea(self):
        return self._len*self._bre

    def getPerimeter(self):
        return 2*(self._len+self._bre)

    def isSquare(self):
        if self._len == self._bre:
            return True
        return False
