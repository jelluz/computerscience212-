# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end if end else True:
        yield i
        i = i + 1


def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    for i in ints(0):
        yield i
        if i > 0:
            yield -i

for i in all_ints():
    print(i)