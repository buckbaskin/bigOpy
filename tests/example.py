from bigo import analyze as a
from random import sample

# inputs: tuple with (args, kwargs)
@a(lambda inputs: len(inputs[0][0]), measure='time')
def sort_me1(list_):
    return sorted(list_)

@a(lambda inputs: len(inputs[0][0]), measure='cpu')
def sort_me2(list_):
    return sorted(list_)

def example_problem(size):
    return sample(list(range(0, size)), k=int(size))

for i in range(0, 6):
    sort_me1(example_problem(10**i))
    sort_me2(example_problem(10**i))

