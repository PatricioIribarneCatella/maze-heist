class Visitor():

    def __init__(self, name, arrival_time, duration):
        self._name = name
        self._arrival_time = int(arrival_time)
        self._duration = int(duration)
        self._departure_time = self._arrival_time + self._duration

    @property
    def name(self):
        return self._name

    @property
    def departure_time(self):
        return self._departure_time

    @property
    def arrival_time(self):
        return self._arrival_time

    def __str__(self):
        return "({0},{1},{2})".format(self._name, self._arrival_time, self._departure_time)

    def __repr__(self):
        return "({0},{1},{2})".format(self._name, self._arrival_time, self._departure_time)

