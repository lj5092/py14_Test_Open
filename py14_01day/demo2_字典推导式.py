# 字典推导式{k:v for i in xxx}
li = ['a', 'b', 'c', 'd', 'e']
dict1 = {i: j for i, j in enumerate(li)}
print("字典推导式：", dict1)

# 集合推导式{i for i in xxx}
res = {i for i in range(10)}
print(res)

# 小练习：将如下cookie转换为字典形式
cookies = "BIDUPSID=FD3227AC89E73C1314FC1C236F5AE7F6; PSTM=1642927329; " \
          "__yjs_duid=1_5faa0dd1b27fb7fa9eb36bf956ce30431644847962243; " \
          "BD_UPN=12314753; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; " \
          "BAIDUID=A4C03E320623C656BDF30796E42CBE70;"

new_dict = {}
new_cookie = cookies.split('; ')
print(new_cookie)
for i in new_cookie:
    k, v = i.split('=')
    new_dict[k] = v
print(new_dict)

# 字典推导式
dict1 = {i.split('=')[0]:i.split('=')[1] for i in cookies.split('; ')}
print("字典推导式：", dict1)

# 推导式的嵌套
dict2 = {v:k for k,v in [i.split('=') for i in cookies.split('; ')]}
print("推导式的嵌套：", dict2) 

# （字典，集合，列表）推导式都支持if和三元运算符

jihe = {"data{}".format(i) if i%2==0 else "lemon{}".format(i) for i in range(20)}
lb = ["data{}".format(i) if i%2==0 else "lemon{}".format(i) for i in range(20)]
print("集合是无序的：", jihe)
print("列表是有序的： ", lb)