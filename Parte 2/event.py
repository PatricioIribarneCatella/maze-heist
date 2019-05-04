class Event():

    def __init__(self, event_type, name, time):
        self._event_type = event_type
        self._name = name
        self._time = time

    @property
    def type(self):
        return self._event_type

    @property
    def visitor(self):
        return self._name

    @property
    def time(self):
        return self._time

    def __repr__(self):
        return "({0}, {1}, {2})".format(self.visitor, self.type, self.time) 
