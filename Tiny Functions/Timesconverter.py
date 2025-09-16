def time(num):
    h = num//3600
    p = num%3600
    m = p//60
    s = p%60
    return f"{h}:{m}:{s}"

print(time(7240))
    