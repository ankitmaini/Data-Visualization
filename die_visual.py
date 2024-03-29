from die import Die
import pygal
# Create a Die with six sides
die = Die()

# Make some rolls and store the results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


# Analyse the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times'
hist.x_labels = [str(x) for x in range(1,7)]
hist._x_title = 'Result'
hist._y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
