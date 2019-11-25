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

# 5 if
numbers = [0, 3, 4, 6]
for num in numbers:
    if num == 3:
        print('find 3')
    else:
        print(num)
for num in numbers:
    if num>1 and num<4:
        print(num)
strings = ['A','B','c']
