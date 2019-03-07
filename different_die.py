from die import Die
import pygal

# Create a D6 and D10
die_1 = Die()
die_2 = Die(10)

# Make some rolls and store the results in a list
results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analyse the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling D6 and D10 dice 5000 times.'
hist.x_labels = [str(x) for x in range(2, 17)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual2.svg')