class Event():

	event = None
	visitor = None

	def __init__(self, event, visitor):
		self.event = event
		self.visitor = visitor

	def get_event(self):
		return self.event

	def get_visitor(self):
		return self.visitor
