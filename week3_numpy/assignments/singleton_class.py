# 1. Singleton using __new__
class SingletonNew:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# 2. Singleton using a decorator
def singleton_decorator(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton_decorator
class SingletonDecor:
    pass

# 3. Singleton using metaclass
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    pass

# Example usage:
if __name__ == "__main__":
    a = SingletonNew()
    b = SingletonNew()
    print("SingletonNew:", a is b)

    c = SingletonDecor()
    d = SingletonDecor()
    print("SingletonDecor:", c is d)

    e = SingletonClass()
    f = SingletonClass()
    print("SingletonMeta:", e is f)
