def gcb(m,n):
    while n:
        m,n=n,m % n
    return m
print(gcb(20,45))
print(gcb(7,9))