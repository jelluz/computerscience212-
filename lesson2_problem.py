# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# Hopper does not live on the top floor.
# Kay does not live on the bottom floor.
# Liskov does not live on either the top or the bottom floor.
# Perlis lives on a higher floor than does Kay.
# Ritchie does not live on a floor adjacent to Liskov's.
# Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.

import itertools


def floor_puzzle():
    # Your code here
    h = lambda h: h < 4
    k = lambda k: k > 0
    l = lambda l: h(l) and k(l)
    pk = lambda p, k: p > k
    rl = lambda r, l: abs(r - l) > 1
    lk = rl

    floors = [0,1,2,3,4]
    for Hopper, Kay, Liskov, Perlis, Ritchie in itertools.permutations(floors):
        if h(Hopper) and k(Kay) and l(Liskov) and pk(Perlis,Kay) and rl(Ritchie,Liskov) and lk(Liskov,Kay):
            return [Hopper, Kay, Liskov, Perlis, Ritchie]


print(floor_puzzle())
