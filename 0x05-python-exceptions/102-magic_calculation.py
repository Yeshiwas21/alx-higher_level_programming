def magic_calculation(a, b):
    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            res += a ** b / i
        except Exception:
            res = b + a
            break
    else:
        res = res / (a - b)
    return res

