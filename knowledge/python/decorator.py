def return_default(value):
    def deco(func):
        def wrapped(*args, **kwargs):
            ret = func(*args, **kwargs)
            if ret is None:
                ret = value
            return ret
        return wrapped
    return deco


@return_default(10)
def at_least_10(x):
    if x >= 10:
        return x


@return_default("python")
def greeting(msg):
    return msg


print(at_least_10(3)) # 10
print(greeting(None)) # "python"