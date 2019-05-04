from bintrees import AVLTree as bst 
from event_type import EventType

class Visitors():

    def __init__(self): 
        self._visitors = set()
        self._departure_times = bst()
        self._arrival_times = bst()

    def __len__(self):
        return len(self._visitors)

    def copy(self):
        return self._visitors.copy()

    def add(self, visitor): 
        self._visitors.add(visitor.name)
        self._departure_times.insert(visitor.departure_key, visitor)
        self._arrival_times.insert(visitor.arrival_key, visitor)

    def remove(self, visitor): 
        self._visitors.remove(visitor.name) 
        self._departure_times.pop(visitor.departure_key) 
        self._arrival_times.pop(visitor.arrival_key)

    @property
    def duration(self):
        return self._departure_times.min_item()[1].departure_time - self._arrival_times.min_item()[1].arrival_time

