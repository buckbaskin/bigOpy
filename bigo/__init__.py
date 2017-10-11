import dis
import sys

from datetime import datetime
from io import StringIO
from time import process_time

runtime_db = {}

def save_runtime(func_name, size, total_millis):
    global runtime_db
    if func_name not in runtime_db:
        runtime_db[func_name] = {}
    if size not in runtime_db[func_name]:
        runtime_db[func_name][size] = []
    print('saving %s, %d, %f' % (func_name, size, total_millis,))
    runtime_db[func_name][size].append(total_millis)

class AbstractTracer(object):
    def __init__(self, func):
        raise NotImplementedError()

    def start(self):
        raise NotImplementedError()

    def end(self):
        raise NotImplementedError()

    def runtime(self):
        raise NotImplementedError()


class CPUTracer(AbstractTracer):
    def __init__(self, func):
        self.accum = 0
        self.__last_accum = self.accum

    def start(self):
        self.accum = 0
        sys.settrace(self._tracer)

    def end(self):
        sys.settrace(None)
        self.__last_accum = self.accum

    def runtime(self):
         return self.__last_accum
    
    def _tracer(self, frame, event, arg):
        with StringIO() as out:
            dis.dis(frame.f_code.co_code, file=out)
            # print(len(out.getvalue().split('\n')))
            self.accum += len(out.getvalue().split('\n'))

        # sys.exit(1)
        if event == 'return':
            print('%5d trace of %s, %s, arg' % (self.accum, frame, event,))
        else:
            print('%5d trace of %s, %s, %s' % (self.accum, frame, event, arg,))
        return self._tracer

class AbstractTimeTracer(AbstractTracer):
    def __init__(self, func):
        self.time = None
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = self.time()

    def end(self):
        self.end_time = self.time()

    def runtime(self):
        try:
            return (self.end_time - self.start_time).total_seconds() * 1000
        except AttributeError:
            return (self.end_time - self.start_time) * 1000

class ProcessTimeTracer(AbstractTimeTracer):
    def __init__(self, func):
        super(ProcessTimeTracer, self).__init__(func)
        self.time = process_time

class TotalTimeTracer(AbstractTimeTracer):
    def __init__(self, func):
        super(TotalTimeTracer, self).__init__(func)
        self.time = datetime.now
        

def analyze(input_sizer, measure='time'):
    if measure=='cpu':
        Tracker = CPUTracer
    else:
        Tracker = ProcessTimeTracer
    def decorator(func):
        tracker = Tracker(func)
        def special_func(*args, **kwargs):
            tracker.start()
            value = func(*args, **kwargs)
            tracker.end()
            save_runtime(func.__name__, input_sizer((args, kwargs,)),
                tracker.runtime())
            return value
        special_func.__name__ = func.__name__
        return special_func
    return decorator

