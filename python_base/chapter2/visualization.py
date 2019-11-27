import matplotlib.pyplot as plt

path = './python_base/chapter2/'
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 设置图标标题，并给坐标轴加上标签
plt.title("square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

plt.plot(input_values, squares, linewidth=5)

plt.show()

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c='red', edgecolors='none',s=40)
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none',s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none',s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()
plt.savefig(path+'squares_plot.png', bbox_inches='tight')


