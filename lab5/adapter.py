import math
 
#Дырка на носке
class HoleInToe(object):
    def __init__(self, r):
        # задаем радиус дыры
        self.r = r
 
    def put(self, obj):
        try:
            if self.r >= obj.r:
                print (u'Перекрывает!')
            else:
                print (u'Не перекрывает')
        except AttributeError:
            print (u'Переданный объект не умеет ничего!')
 
 
class Patch(object):
    def __init__(self, x, h):
        self.x = x
        self.h = h
 
 
class SquareHoleAdapter(object):
    def __init__(self, sq_obj):
        self.sq_obj = sq_obj
 
    @property
    def r(self):
        return math.sqrt(2*(self.sq_obj.x**2))/2
 
 
h1 = HoleInToe(5)
h2 = HoleInToe(2)
s1 = Patch(5, 7)
s2 = Patch(3, 3)
sa = SquareHoleAdapter(s2)
 
h1.put(s1)
#print('Переданный объект не умеет вычислять радиус дырки, в которую он влезет! Напишите Адаптер на python!')
 
h1.put(sa)
#print('Лезет!')
 
h2.put(sa)
#print('Не лезет')