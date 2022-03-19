def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3))

# 파이썬의 bisect.bisect 메소드를 사용하면 이 코드를 간략하게 만들 수 있습니다.

import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))