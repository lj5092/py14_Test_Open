import pytest


@pytest.mark.parametrize('item', [11, 22, 33])
def test_demo(item):
    print("item:", item)

# 带参数的装饰器，在装饰的时候，实际上是先调用@后边的方法，把调用的结果在用来装饰下面的函数或(类)
result = pytest.mark.parametrize('item', [11, 22, 33])
test_demo = result(test_demo)


def decorator(item):
    def wrapper(*args, **kwargs):
        # 功能扩展
        result = item(*args, **kwargs)
        # 功能扩展
        return result
    return wrapper


def musen(age, sex):
    return decorator


@musen(18, '男')
def work():
    print("-----work------")

# 装饰器如何使用参数
# 需要三层函数的嵌套


def musen(age, sex):
    # 最外层的参数，是装饰器的参数
    def decorator(item):
        # 中间层的参数，是接受被装饰的函数
        def wrapper(*args, **kwargs):
            # 最里层的参数，接受的是被装饰函数调用时传递的参数
            print("装饰器扩展的功能代码111，age", age)
            result = item(*args, **kwargs)
            print("装饰器扩展的功能代码111，sex", sex)
            return result
        return wrapper
    return decorator


@musen(18, '男')
def work(a, b):
    print("-----work------")
    print('a+b= {}'.format(a+b))



work(11, 12)