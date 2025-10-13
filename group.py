"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group ={
    "Ashley": {
        "age": 22,
        "job": "student",
        "connections": {
            "friend": ["Meng"],
            "partner": ["Meng"]
        }
    },
    "Meng": {
        "age": 23,
        "job": "student",
        "connections": {
            "friend": ["Ashley"],
            "landlord": ["Ashley"]
        }
    },
    
}

def forget(person1, person2):
    """Removes all connections from person1 to person2."""
    if person1 in my_group:
        person1_connections = my_group[person1]["connections"]
        for relationship_type in list(person1_connections.keys()):
            if person2 in person1_connections[relationship_type]:
                person1_connections[relationship_type].remove(person2)
                # If the list becomes empty, you can optionally remove the relationship_type key
                if not person1_connections[relationship_type]:
                    del person1_connections[relationship_type]


def add_person(name, age, job, relations):
    """Adds a new person to the group with their details and connections."""
    if name not in my_group:
        my_group[name] = {
            "age": age,
            "job": job,
            "connections": relations
        }
    else:
        print(f"Error: {name} already exists in the group.")

def average_age():
    """Calculates and returns the average age of everyone in the group."""
    if not my_group:
        return 0
    
    total_age = 0
    num_people = 0
    
    for person in my_group.values():
        if "age" in person:
            total_age += person["age"]
            num_people += 1
            
    if num_people == 0:
        return 0
    
    return total_age / num_people





