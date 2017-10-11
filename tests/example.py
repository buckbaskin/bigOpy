from bigo import analyze as a
from random import sample

# inputs: tuple with (args, kwargs)
@a(lambda inputs: len(inputs[0][0]), measure='time')
def sort_me(list_):
    print('list_, %d' % len(list_))
    return sorted(list_)

def example_problem(size):
    return sample(list(range(0, size)), k=int(size))

for i in range(0, 6):
    sort_me(example_problem(10**i))

