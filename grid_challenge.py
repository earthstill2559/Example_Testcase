def testgridChallenge(a):
    if len(a) > 100 or len(a) < 1:
        return 'Error'

    for i in range(len(a)):
        s = sorted((list(a[i])))
        a[i] = s
    
    for i in range(1,len(a)):
        for j in range(1,len(a[i])):
            if a[j-1][i-1] > a[j][i-1]:
                return 'NO'
    return 'YES'