
def __call(f):
    if type(f) == list:
        args = tuple(f[1:])
        f[0](*args)
    else:
        f()

def Run(aliases, sequence):
    begin = aliases[sequence['ws_start']] if type(sequence['ws_start']) == str else sequence['ws_start']
    ret = __call(begin)
