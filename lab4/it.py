class IteratorBase(object):
    """Базовый класс итератора"""
    def first(self):
        raise NotImplementedError() #1-й элемент
 
    def last(self):
        raise NotImplementedError() #Последний элемент
 
    def next(self):
        raise NotImplementedError()
 
    def prev(self):
        raise NotImplementedError()
 
    def current_item(self):
        raise NotImplementedError()
 
    def is_done(self, index):
        raise NotImplementedError()
 
    def get_item(self, index):
        raise NotImplementedError()
 
 
class Iterator(IteratorBase):
    def __init__(self, list_=None):
        self._list = list_ or []
        self._current = 0
 
    def first(self):
        return self._list[0]
 
    def last(self):
        return self._list[-1]
 
    def current_item(self):
        return self._list[self._current]
 
    def is_done(self, index):
        last_index = len(self._list) - 1
        return 0 <= index <= last_index
 
    def next(self):
        self._current += 1
        if not self.is_done(self._current):
            self._current = 0
        return self.current_item()
 
    def prev(self):
        self._current -= 1
        if not self.is_done(self._current):
            self._current = len(self._list) - 1
        return self.current_item()
 
    def get_item(self, index):
        if not self.is_done(index):
            raise IndexError('Нет элемента с индексом: %d' % index)
        return self._list[index]
 
 
it = Iterator(('one', 'two', 'three', 'four', 'five'))
print ([it.prev() for i in range(5)])  # ['five', 'four', 'three', 'two', 'one']
print ([it.next() for i in range(5)]) # ['two', 'three', 'four', 'five', 'one']