from datetime import datetime

runtime_db = {}

def save_runtime(func_name, size, total_millis):
    global runtime_db
    if func_name not in runtime_db:
        runtime_db[func_name] = {}
    if size not in runtime_db[func_name]:
        runtime_db[func_name][size] = []
    print('saving %s, %d, %f' % (func_name, size, total_millis,))
    runtime_db[func_name][size].append(total_millis)

def analyze(input_sizer, measure='time'):
    print('analyze a function!')
    def decorator(func):
        print('decorate func %s' % (func.__name__,))
        def special_func(*args, **kwargs):
            print('start time')
            start = datetime.now()
            value = func(*args, **kwargs)
            end = datetime.now()
            runtime = (end - start).total_seconds() * 1000
            save_runtime(func.__name__, input_sizer((args, kwargs,)),
            runtime)
            print('end time')
            return value
        special_func.__name__ = func.__name__
        return special_func
    return decorator

