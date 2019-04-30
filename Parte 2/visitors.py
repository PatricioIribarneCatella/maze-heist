class Visitors():

	visitors = None
	earliest_arrival_visitor = None

	def __init__(self, event, visitor):
		self.visitors = []

	def __len__(self):
		return len(self.visitors)

	def get_copy():
		return self.visitors.copy()

	def add(self, visitor):
		self.visitors.append(visitor)
		if(visitor.get_arrival_time() < self.earliest_arrival_visitor.get_arrival_time()):
			self.earliest_arrival_visitor = visitor

	def remove(self, visitor):
		self.visitors.append(visitor)
		if(self.earliest_arrival_visitor == visitor):
			self._find_new_earliest_arrival_visitor()

	def _find_new_earliest_arrival_visitor(self):
		self.earliest_arrival_visitor = None
		for visitor in visitors:
			if not self.earliest_arrival_visitor or visitor.get_arrival_time() < self.earliest_arrival_visitor.get_arrival_time():
				self.earliest_arrival_visitor = visitor

	def get_groups_duration(visitor):
		return (visitor.get_departure_time() - self.earliest_arrival_visitor)
