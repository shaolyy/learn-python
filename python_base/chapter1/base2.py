# 函数
def print_params(place_param, de_params='haha', *args, **kw):
    """print all params"""
    print(place_param, de_params)
    for param in args:
        print(param)
    for key, value in kw.items():
        print(key, value)
args = ('first_arg', 'secend_arg')
kw = {'first_kw': 'first', 'second_kw': 'second'}
print_params('place', 'default', *args, **kw)

# 文件
filepath = 'pi.txt'
with open(filepath, "r+") as file:
    num = list(range(30))
    file.write(str(num))