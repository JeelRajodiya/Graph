def reversed_range(n):
    x=0
    while True:
        yield n
        n-=1
        if x==n+1:
            break
