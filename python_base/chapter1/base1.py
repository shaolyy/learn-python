# 
name = 'ada lovelace'
print(name.lower(),name.upper(), name.title())

name = '  ad lovelace   '
print(name, len(name),'\n', name.rstrip(), len(name.rstrip()), '\n',
        name.lstrip(),len(name.lstrip()),'\n', name.strip(), len(name.strip()))


# 3 list
# 访问
names = ['Bob','Tom']
ways = ['car', 'bike']
for name_i in range(len(names)):
    for way in ways:
        print(names[name_i] + ' like ' + way)

# 修改、添加、删除
names[0] = 'White'
ways.append('walk')
ways.insert(0, 'fly')
print('ways_append_insert: ', ways)
del ways[0]
ways.remove('car')
poped = ways.pop()
print('ways_del_remove_pop:', ways, ' poped:', poped)

# 3-4...3-7
def print_names(guest_names):
    for name in guest_names:
        print('Dear ' + name + ', tank you!')
guest_names = ['a', 'b', 'c']
print_names(guest_names)
print(guest_names[1] + ' can not join!')
guest_names[1] = 'd'
print_names(guest_names)
print('Find a bigger table!')
guest_names.insert(0, 'e')
guest_names.insert(2, 'f')
guest_names.append('g')
print_names(guest_names)
print('Sorry, just two people!')
for i in range(len(guest_names) - 2):
    poped_name = guest_names.pop()
    print('Sorry, ' + poped_name)
print_names(guest_names)
while len(guest_names) > 0:
    del guest_names[0]
print(guest_names)


# 列表组织
cars = ['bmw', 'audi', 'toyota', 'subaru']
# sorted() 返回排序后的列表，原列表不变
print('cars:\t\t', cars, '\nsorted(cars):\t', sorted(cars),'\ncars:\t\t', cars)
# list.sort()对列表永久排序
cars.sort()
print('cars.sort():\t', cars,'\ncars:\t\t', cars )
# reverse()方法反转列表排序，sorted可以传递reverse为True反转排序后列表
print(sorted(cars, reverse=True))
print(cars)
cars.reverse()
print(cars)
print('len_cars:', len(cars),'the last car:', cars[-1])


# 4 list tuple
# for 循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# range()
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print(max(even_numbers), min(even_numbers), sum(even_numbers))

# 列表解析
squares = [value**2 for value in range(1, 7)]
print(squares)
# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:4:2])
print(players[4:0:-2])
# 复制列表
orign_l = [1, 2, 3, 4]
print(orign_l)
copy_l = orign_l
print(copy_l)
copy_l_  = orign_l[:]
print(copy_l_)
orign_l.append(5)
print('orign:\t',orign_l, '\n=:\t',copy_l,'\n[:]:\t', copy_l_)
print(id(orign_l), id(copy_l), id(copy_l_))

# 元组
orign_t = (3, 5)
print(orign_t)
# 元组元素不可修改，但元组元素若包含可变量，则可以修改可变量内的元素
l = [1, 3]
orign_t = (l, 3)
print(orign_t)
orign_t[0][0] = 6
print(orign_t)

# 5 if while break continue
numbers = [0, 3, 4, 6]
for num in numbers:
    if num == 3:
        print('find 3')
    else:
        print(num)
for num in numbers:
    print(num)
    if num>1 and num<4:
        break
strings = ['A','B','c']



# dict

# 创建
alien_0 = {'color': 'green', 'points': 5}
alien_1 = dict({'color': 'green', 'points': 5})
# 使用可迭代对象
lang = (['a',1], ['b', 3])
alien_2 = dict(lang)     
alien_3 = dict((('a',1), ('b', 2)))
# 使用fromkeys
alien_4 = {}.fromkeys(['a','b', 'c'], None)
print(alien_0, alien_1, alien_2, alien_3, alien_4)
# 访问
print(alien_0['color'])
print(alien_0.get('x', -1))        # get无keyerror
# 遍历
for key, value in alien_0.items():
    print(key, value)
for key in alien_0.keys():
    print(key)
for value in alien_0.values():
    print(value)
# 增
alien_0['speed'] = 'slow'
alien_0.update({'x':45})
print(alien_0)
# 改
alien_0['speed'] = 'medium'
print(alien_0)
alien_0.setdefault('x',50)      # 若存在则更新值，不存在则创建
print(alien_0)
# 删除
# del pop popitem
del alien_0['x']        
print(alien_0.pop('speed'))     # pop有keyerror
# 清空
del alien_1         # alien_1 完全删除 
alien_2.clear()
print(alien_2)


# set
s1 = set(alien_4.keys())
print(s1)
s2 = {3,'a'}
print(s2, type(s2))
print(s1 | s2, s1 & s2, s1 - s2)
s1.add('d')
s1.update([1, 2, 3])        # updae(seq)
print(s1)
# remove有keyerror， discard无
print(s1.remove(1), s1.discard(1))
print(s1)
print(s1.pop())
s1.clear()
print(s1)

