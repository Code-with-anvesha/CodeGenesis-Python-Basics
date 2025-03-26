import json

EVENTS_FILE = "events.json"

def load_events():
    #Loads events from the JSON file
    try:
        with open(EVENTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_events(events):
    #Saves events to the JSON file
    with open(EVENTS_FILE, "w") as file:
        json.dump(events, file, indent=4)

def add_event(date, event):
    
    events = load_events()
    if date in events:
        events[date].append(event)
    else:
        events[date] = [event]
    save_events(events)
    print("Event added successfully!")

def view_events():
    #Displays all events
    events = load_events()
    if not events:
        print("No events found!")
    else:
        for date, event_list in events.items():
            print(f"{date}: {', '.join(event_list)}")

if __name__ == "__main__":
    add_event("2025-02-03", "Friend's Birthday")
    view_events()
