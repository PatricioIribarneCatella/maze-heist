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

    @property
    def departure_key(self):
        return self._departure_time * 10**9 + abs(hash(self._name)) % 10**8

    @property
    def arrival_key(self):
        return self._arrival_time * 10**9 + abs(hash(self._name)) % 10**8

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        return self._name == other._name

    def __str__(self):
        return "({0},{1},{2})".format(self._name, self._arrival_time, self._departure_time)

    def __repr__(self):
        return "({0},{1},{2})".format(self._name, self._arrival_time, self._departure_time)
