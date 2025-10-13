"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

group_of_friends ={
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

# 1. The maximum age of people in the group
max_age = max([person["age"] for person in group_of_friends.values()])
print(f"The maximum age of people in the group is: {max_age}")

# 2. The average (mean) number of relations among members of the group
total_relations = sum([len(relations_dict) for relations_dict in [person["connections"] for person in group_of_friends.values()]])
# Note: The number of relations is the number of keys in the connections dictionary
average_relations = total_relations / len(group_of_friends)
print(f"The average number of relations is: {average_relations:.2f}")

# 3. The maximum age of people with at least one relation
# Filter people who have at least one connection
people_with_relations = [person for person in group_of_friends.values() if person["connections"]]
# Then find the max age among them
if people_with_relations:
    max_age_with_relation = max([person["age"] for person in people_with_relations])
    print(f"The maximum age of people with at least one relation is: {max_age_with_relation}")
else:
    print("No one in the group has any relations.")

# 4. The maximum age of people with at least one friend
# Filter people who have a 'friend' key in their connections dictionary
people_with_friends = [person for person in group_of_friends.values() if "friend" in person["connections"]]
# Then find the max age among them
if people_with_friends:
    max_age_with_friend = max([person["age"] for person in people_with_friends])
    print(f"The maximum age of people with at least one friend is: {max_age_with_friend}")
