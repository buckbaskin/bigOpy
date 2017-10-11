from bigo import analyze

# inputs: tuple with (args, kwargs)
# @analyze(lambda inputs: len(inputs[0][0], measure='time')
def sort_me(list_):
    return sorted(list_)

print(type(sort_me))
assert sort_me.__name__ == 'sort_me'
