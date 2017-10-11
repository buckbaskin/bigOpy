
def analyze(input_sizer, measure='cpu'):
    def decorator(func):
        def special_func(*args, **kwargs):
            return func(*args, **kwargs)
        special_func.__name__ = func.__name__
        return special_func
    return decorator

