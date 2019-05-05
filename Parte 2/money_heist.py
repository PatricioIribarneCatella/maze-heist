import csv
from visitor import Visitor
from visitors import Visitors
from event import Event
from event_type import EventType 

def get_visitors_from_records_file(filename):
    
    with open(filename) as records_file:
        records = csv.reader(records_file)
        visitors = { record[0]: Visitor(*record) for record in records }
        
    return visitors

def generate_events(visitors):

    events = []

    for visitor in visitors.values():
        arrival = Event(EventType.ARRIVAL, visitor.name, visitor.arrival_time)
        departure = Event(EventType.DEPARTURE, visitor.name, visitor.departure_time)
        events.extend([arrival, departure])

    events.sort(key=lambda event: event.time, reverse=True)

    return events

def find_suspects(records_file, min_ind, max_ind, min_dur, max_dur):

    visitors = get_visitors_from_records_file(records_file)
    events = generate_events(visitors)

    possible_gangs = []
    current_gang = Visitors() 

    i = 0
    while i < len(events):
        current_time = events[i].time  
        
        has_departure = False
        while i < len(events) and events[i].time == current_time: 
            event = events[i]
            has_departure |= event.type == EventType.DEPARTURE
            current_gang.add(visitors[event.visitor]) if event.type == EventType.DEPARTURE else current_gang.remove(visitors[event.visitor]) 
            i += 1

        if has_departure and min_ind<=len(current_gang)<=max_ind and min_dur<=current_gang.duration<=max_dur: 
            possible_gangs.append(current_gang.copy())
       
    return possible_gangs


individuals_limits = [2,3]
duration_limits = [1,2]
print(find_suspects("records2.csv", *individuals_limits,*duration_limits))
