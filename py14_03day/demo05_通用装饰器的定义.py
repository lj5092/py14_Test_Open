# 通用装饰器
def decorator(func):
    def wrapper(*args, **kwargs):
        print("装饰器扩展功能")
        result = func(*args, **kwargs)
        return result
    return wrapper


# 例子
def tongyong(fun):
    def work1(*args, **kwargs):
        print("装饰器的拓展功能")
        result = fun(*args, **kwargs)
        return result
    return work1


@tongyong
def work2(a, b, c):
    print('a: ', a)
    print('b: ', b)
    print('c: ', c)
    return a,b,c




if __name__ == '__main__':
    print(work2(1,2,3))