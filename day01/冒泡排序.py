lis = [56,78,34,45,55,23,-53,48,35,754,32,63]

def sortport():
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis [j] > lis[j+1]:
                lis [j],lis[j+1] = lis [j+1],lis[j]
    return lis

sortport()
print(lis)