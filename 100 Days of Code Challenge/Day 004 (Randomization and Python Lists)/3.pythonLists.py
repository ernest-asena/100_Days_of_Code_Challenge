# A list is a data structure in Python
# square brackets and stores multiple items
states = ['Texas', 'North Dakota', 'DC', 'Chicago', 'Atlanta']

print(states)
print(states[0])  # what's the first item in the list?
print(states[-1])  # what's the last item in the list?
print(states[-5])  # what's the first item in the list?
print(states[-2])  # what's the second last item in the list?

# change a value in the list
states[1] = 'North Carolina'
print(states)

# add an item to the list
states.append('Alabama')
print(states)

states.extend(['Colorado', 'Alaska', 'Michigan', 'Missouri'])
print(states)
