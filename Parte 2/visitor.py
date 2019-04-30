class Visitor():

	arrival_time = None
	departure_time = None
	duration = None
	name = None

	def __init__(self, name, arrival_time, duration):
		self.name = name
		self.arrival_time = int(arrival_time)
		self.duration = int(duration)
		self.departure_time = self.arrival_time + self.duration

	def get_departure_time(self):
		return self.departure_time
