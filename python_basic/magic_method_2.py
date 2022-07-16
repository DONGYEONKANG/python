# Special(Magic) Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 클래스안에 정의할 수 있는 특별한 메서드

# 클래스 예제2
# 벡터()
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 - (50, 15)
# Max((5, 10)) = 10

class Vector(object):
    def __init__(self, *args):
        '''
        Create a Vector, example: v = Vector(5,10)
        '''
        
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args
            
    def __repr__(self):
        """
        Return the vector informations

        """
        return "Vector({}, {})".format(self._x, self._y) 
    
    def __add__(self, other):
        """Return the vector addition of self and other"""
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)
    
    def __bool__(self):
        return bool(max(self._x, self._y))

    
# vector instance
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()    
    

# 메직 메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)


print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(bool(v1))

