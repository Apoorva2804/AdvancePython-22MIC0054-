print("Welcome to Apoorva's Travel Planner with Collaborative Filtering!\n")

# User Database
past_users = {
    "Apoorva": ["Paris", "Eiffel Tower", "Louvre Museum", "Wine Tasting", "Seine Cruise"],
    "Ved":   ["Paris", "Montmartre Walk", "Seine Cruise", "French Breakfast", "Eiffel Tower"],
    "Arnav": ["London", "Big Ben", "Thames River", "Paris", "Louvre Museum"],
    "Rachna": ["Paris", "Eiffel Tower", "Notre-Dame", "French Breakfast"],
}

# Input Destination 
user_itinerary = []
destination = input("Enter your destination: ")
user_itinerary.append(destination)
print("\n After append():", user_itinerary)

# Find Similar Users (Using Collaborative Filters)
similar_users = [user for user, places in past_users.items() if destination in places]
print(" Similar users found:", similar_users)

# Collaborative Filter recommendation 
recommendations = []
for user in similar_users:
    recommendations.extend(past_users[user])

# Filter Recommendations 
filtered = []
for place in recommendations:
    if place not in user_itinerary and place not in filtered:
        filtered.append(place)

# Ensure at least 3 unique entries
while len(filtered) < 3:
    fallback = ["Local Market Tour", "Museum Visit", "City Walk", "Cooking Class"]
    for f in fallback:
        if f not in filtered and f not in user_itinerary:
            filtered.append(f)
        if len(filtered) >= 3:
            break

# Add Top 5 to Itinerary 
user_itinerary.extend(filtered[:5])
print(" After extend():", user_itinerary)

# Optional Insert
insert_item = input("\nEnter a must-do activity to insert at position 1: ")
user_itinerary.insert(1, insert_item)
print(" After insert():", user_itinerary)

# Optional Remove
remove_item = input("Enter an item to remove (or press Enter to skip): ")
if remove_item in user_itinerary:
    user_itinerary.remove(remove_item)
    print(" After remove():", user_itinerary)

# Optional Pop
if len(user_itinerary) > 2:
    do_pop = input("Do you want to remove the last item on list? (yes/no): ").lower()
    if do_pop == "yes":
        removed = user_itinerary.pop()
        print(f" Removed '{removed}' using pop()")
        print("Itinerary now:", user_itinerary)

# Use of index
item_to_find = input("Enter an item to find its position: ")
if item_to_find in user_itinerary:
    idx = user_itinerary.index(item_to_find)
    print(f" Index of '{item_to_find}': {idx}")

# Count of object in list
item_to_count = input("Enter an item to count how many times it appears: ")
print(f" '{item_to_count}' appears {user_itinerary.count(item_to_count)} time(s)")

# Sorted and Reversed List
sorted_itinerary = user_itinerary.copy()
sorted_itinerary.sort()
print(" Sorted itinerary:", sorted_itinerary)

reversed_itinerary = user_itinerary.copy()
reversed_itinerary.reverse()
print(" Reversed itinerary:", reversed_itinerary)

# Backup
backup = user_itinerary.copy()
print(" Backup itinerary copy:", backup)

#Final Output 
print("\n Final Personalized Itinerary:", user_itinerary)
