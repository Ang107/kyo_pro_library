def isOK(mid):
    pass


def meguru(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    return ok
