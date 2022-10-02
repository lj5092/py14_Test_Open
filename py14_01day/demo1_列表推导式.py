# 推导式是用来生成数据的简介的语法

# 列表推导式[i for i in xx]
list_one = ['data{}'.format(i) for i in range(99)]
print("列表推导式：", list_one)

# 推导式结合if对数据进行过滤
list1 = [i for i in range(50) if i % 5 == 0]
print(list1)

list2 = ['page{}'.format(i+1) for i in range(10)]
print(list2)

# 三元运算符+for循环,data=[data0,lemon1,data2,lemon3]
list3 = ['data{}'.format(i) if i%2==0 else 'lemon{}'.format(i) for i in range(100)]
print("带三元运算符的列表推导式：", list3)

