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
        count_departure = self._departure_times.get(visitor.departure_time, 0)
        count_arrival = self._arrival_times.get(visitor.arrival_time, 0)
        self._departure_times.insert(visitor.departure_time, count_departure + 1)
        self._arrival_times.insert(visitor.arrival_time, count_arrival + 1)

    def remove(self, visitor): 
        self._visitors.remove(visitor.name)
        count_departure = self._departure_times.get(visitor.departure_time)
        count_arrival = self._arrival_times.get(visitor.arrival_time)
        if (count_departure == 1): self._departure_times.pop(visitor.departure_time) 
        else: self._arrival_times.insert(visitor.departure_time, count_departure - 1)
        if (count_arrival == 1): self._arrival_times.pop(visitor.arrival_time)
        else: self._arrival_times.insert(visitor.arrival_time, count_arrival - 1)


    @property
    def duration(self):
        return min(self._departure_times)- min(self._arrival_times)

