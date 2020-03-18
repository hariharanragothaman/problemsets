def shorten(str1):
    length = len(str1)
    if length < 10:
        return str1
    else:
        ll = length - 2
        lstr1 = [c for c in str1]
        res = ''.join(c for c in lstr1[0]+str(ll)+lstr1[-1])
        return res

if __name__ == '__main__':
    res = shorten(str1)
    print(res)