def _in_improvement(s, xxs, pps, nns, l, i, pl):
    if len(xxs) == 0:
        return l == s
    x,xs  = xxs[0], xxs[1:]
    p,ps  = pps[0], pps[1:]
    n,ns  = nns[0], nns[1:]
    if l == s:
        return True
    else:
        if len(xxs) < l-s:
            return False
        else:
            if pl == x:
                return _in_improvement(s + 1, xs, ps, ns, l, i, pl)
            else:
                return _calc_is_one_move_improvable(xxs, pps, nns, i, i, pl)
def _calc_is_one_move_improvable(xxs, pps, nns, l, i, pl):
    if len(xxs) == 0:
        return l == 0
    x,xs  = xxs[0], xxs[1:]
    p,ps  = pps[0], pps[1:]
    n,ns  = nns[0], nns[1:]
    if len(xxs) <= l:
        return False
    if x == pl:
        return _calc_is_one_move_improvable(xs, ps, ns, (l - 1), i, pl)
    else :
        if (p == pl or n == pl):
            return _in_improvement(0, xs, ps, ns, l, i, pl)
        else:
            return _calc_is_one_move_improvable(xs, ps, ns, i, i, pl)
def is_one_move_improvable(xs, ps, ns, l, pl):
    return  _calc_is_one_move_improvable(xs, ps, ns, l, l, pl)

casos = [
    (2, True, [ [0, 1, 1, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0] ] ),
    (2, True, [ [1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0] ] ),
    (2, True, [ [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0] ] ),
    (2, True, [ [0, 0, 0, 1, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0] ] ),
    (2, True, [ [0, 0, 1, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0] ] ),
    (2, True, [ [0, 0, 1, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0] ] ),
    (2, False, [ [1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0] ]),
    (2, False, [ [1, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0] ]),
    (2, False, [ [0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0] ]),
    (2, False, [ [0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0] ]),
 # 3
    (3, True, [[1, 1, 1, 0, 0],
               [0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0]]),
    (3, True, [[0, 1, 1, 1, 0],
               [1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]),
    (3, True, [[0, 1, 1, 1, 0],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]]),
    (3, True, [[1, 1, 0, 1, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0]]),
    (3, True, [[1, 0, 1, 1, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]),
    (3, True, [[0, 1, 1, 1, 0],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]]),
    (3, True, [[0, 1, 1, 0, 1],
               [0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0]]),
    (3, True, [[0, 0, 1, 1, 1],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]),
    (3, True, [[0, 1, 0, 1, 1],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0]]),
    (3, False, [[1, 1, 0, 0, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0]]),
    (3, False, [[1, 1, 0, 0, 1],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0]]),
    (3, False, [[1, 0, 0, 1, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0]]),
# 4
    (4, True, [[1, 1, 1, 1, 0],
               [0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]]),
    (4, True, [[1, 1, 1, 0, 1],
               [0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0]]),
    (4, True, [[1, 1, 0, 1, 1],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0]]),
    (4, True, [[1, 0, 1, 1, 1],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]),
    (4, True, [[0, 1, 1, 1, 1],
               [1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]),
    (4, False, [[0, 1, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]]),
    (4, False, [[1, 0, 0, 1, 1],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]]),
    (4, False, [[1, 0, 0, 1, 1],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]]),
    (4, False, [[1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]),
]

def iterative_iomi(xxs, pps, nns, l, pl):
    i = l
    f = False
    col = 0
    s = 0
    while col < 5:
        if not f:
            if xxs[col] == pl:
                col += 1
                if l > 0 :
                    l -= 1
            elif pps[col] == pl or nns[col] == pl:
                f = True
                s = 0
                col += 1
            else:
                col += 1
                l = i
        else:
            if l == s:
                return True
            if 5-col < l-s:
                return False
            elif pl == xxs[col]:
                s += 1
                col += 1
            else :
                f = False
                l = i

    return (f and l == 0 ) or (f and l == s)


#
# c = [[0, 1, 1, 1, 1],
#      [0, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0]]
# print (is_one_move_improvable(c[0], c[1], c[2], 4, 1))
#
# print (iterative_iomi(c[0], c[1], c[2], 4, 1))

i = 0
for caso in casos:
    l, expected, c = caso
    # if is_one_move_improvable(c[0], c[1], c[2], l, 1) != expected:
    value = iterative_iomi(c[0], c[1], c[2], l, 1)
    if value != expected:
        print("** ERROR Case : %s" % i)
        print(" -> len: %s" % l)
        print(" -> expected value: %s" % expected)
        print(" -> returned value: %s" % value)
        print(c[0])
        print(c[1])
    # else :
    #     print("Case %s " % i )
    #     print(" -> len: %s" % l)
    #     print(" -> value: %s" % value)
    #     print(c[0])
    #     print(c[1])
    #     print("OK" )

    i += 1

