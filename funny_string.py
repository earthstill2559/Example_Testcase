def funny_string(a):
    if len(a) >= 2 and len(a) <= 10000:
        r = a[::-1]
        for i in range(1, len(a)):
            reverse =  abs(ord(r[i]) - ord(r[i-1]))
            not_reverse = abs(ord(a[i]) - ord(a[i-1]))
            if not_reverse != reverse:
                return 'Not Funny'
            else:
                return 'Funny'
    else:
        return 'not at all'