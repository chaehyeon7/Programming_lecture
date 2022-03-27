# 예) 2차원 평면 위의 점을 나타내는 Coord 클래스의 인스턴스를 (x 값, y 값)으로 출력하기

class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

point = Coord(1, 2)
print( '({}, {})'.format(point.x, point.y) )

# 또는
def print_coord(coord):
    print( '({}, {})'.format(coord.x, coord.y) )
print_coord(point)


# 파이썬에서는 __str__ 메소드를 사용해 class 내부에서 출력 format을 지정할 수 있습니다.

class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)

point = Coord(1, 2)