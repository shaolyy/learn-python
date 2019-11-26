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
filepath = './python_base/chapter1/pi.txt'
with open(filepath, "r+") as file:
    str1 = 'I love programming.\n'
    str2 = "I love creating new games.\n"
    file.write(str1)
    file.write(str2)

try:
    with open(filepath) as f:
        for i in f.readlines():
            print(i.rstrip())
except:
    pass