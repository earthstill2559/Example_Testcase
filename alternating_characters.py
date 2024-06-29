def alternating(s):
    if len(s) >= 1 and len(s) <= 100000:
        ans = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                ans = ans + 1
        return ans
    else:
        return 'Error'