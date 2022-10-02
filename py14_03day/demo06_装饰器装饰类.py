# 装饰类，是在类进行实例化的时候做功能扩展
def decorator(item):

    def wrapper(*args, **kwargs):
        # 功能扩展
        result = item(*args, **kwargs)
        # 功能扩展
        return result
    return wrapper


@decorator
class TestDemo:
    pass