from collections import deque
from visitor import Visitor
from event import Event

def generate_list_sorted_by_arrival_time():

	raw_visitors = open("visitors/%s" % file_visitors)
	csv_visitors = csv.reader(raw_suspects)

	visitors = []

	for csv_visitor in csv_visitors:
		name, arrival_time, duration = csv_visitor
		visitor = Visitor(name, arrival_time, duration)
		visitors.append(visitor)

	return visitoris

def generate_list_sorted_by_departure_time(visitors):

	return sorted(visitors, key=lambda visitor: visitor.get_departure_time())

def generate_event_list(arrival_times, departure_times):
	events = []
	while arrival_times or departure_times:
		if arrival_times[0].get_arrival_time() < departure_times[0].get_departure_time():
			element = Element("arrival", arrival_times.pop(0))
			events.append(element)
		else:
			element = Element("departure", departure_times.pop(0))
			events.append(element)

def find_suspects():

	arrival_time_list = generate_list_sorted_by_arrival_time()
	departure_time_list = generate_list_sorted_by_departure_time()

	events = generate_event_list()

	visitors = Visitors()

	possible_suspects_gangs = []

	for element in events:
		if element.get_event() == "arrival":
			Visitors.add(element)
	else:
		if len(visitors) in range(5,10) and visitors.get_groups_duration(element.get_visitor()) in range(40, 120):
			possible_suspects_gangs.append(visitors.get_copy())
		visitors.remove(element)
