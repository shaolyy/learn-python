from random import randint
import pygal

class Die():
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """"返回一个1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)

path = './python_base/chapter2/'
die = Die()
results = []
for roll in range(1000):
    result = die.roll()
    results.append(result)
#print(results)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()
hist._title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file(path+'die_visual.svg')