
class BerriesVisitor(object):
    """Посетитель"""
    def draw(self, berries):
        methods = {
            Blueberry: self.draw_blueberry,
            Blackberry: self.draw_blackberry,
        }
        draw = methods.get(type(berries), self.draw_unknown)
        draw(berries)
 
    def draw_blueberry(self, berries):
        print ('Голубика')
 
    def draw_blackberry(self, berries):
        print ('Ежевика')
 
    def draw_unknown(self, berries):
        print ('Ягода')
 
 
class Berries(object):
    def draw(self, visitor):
        visitor.draw(self)
 
 
class Blueberry(Berries):
    """Голубика"""
 
 
class Blackberry(Berries):
    """Ежевика"""
 
 
class Сurrant(Berries):
    """Смородина"""
 
 
visitor = BerriesVisitor()
 
blueberry = Blueberry()
blueberry.draw(visitor)
 
blackberry = Blackberry()
blackberry.draw(visitor)
 
currant = Сurrant()
currant.draw(visitor)
