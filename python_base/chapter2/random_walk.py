from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """"一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):
        """"初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
            direction = choice([1, -1])
            distance = choice([0, 1, 2, 3, 4])
            step = direction*distance
            return step

    def fill_walk(self):
        """"计算随机漫步包含的所有点"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step==0 and y_step==0:
                continue

            x_next = self.x_values[-1] + x_step
            y_next = self.y_values[-1] + y_step

            self.x_values.append(x_next)
            self.y_values.append(y_next)
while True:
    rand_walk = RandomWalk(50000)
    rand_walk.fill_walk()
    point_num = list(range(rand_walk.num_points))
    # 设置图像大小
    plt.figure(dpi=1080, figsize=(10, 6))
    plt.scatter(rand_walk.x_values, rand_walk.y_values, c=point_num,
                cmap=plt.cm.Blues,s=1)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_runing = input("Make anther walk? (y/n) :")
    if keep_runing == "n":
        break