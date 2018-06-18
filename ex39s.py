# A dictionary example
# mapping and associating is the key concept in a dictionary

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': "San Francisco",
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('_' * 10) # this print a separated line
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('_' * 10)
print("Michigan's abbrebviation is: ", states['Michigan'])
print("Florida's abbrebviation is: ", states['Florida'])

# do it by using the state then citied dictionary
print('_' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in stare
print('_' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('_' * 10)
# safely get abbreviation by state that might not be there
state = states.get('Texas') # The method get(key, [return value]) returns a value for the given key. If key is not available then returns default value.

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}.")
