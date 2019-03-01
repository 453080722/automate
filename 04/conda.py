def conda(ls):
    st = ""
    for s in ls:
        if s == ls[-2]:
            st = st + s + ',and '
        elif s == ls[-1]:
            st = st + s
        else:
            st = st + s +','
    print(st)
    return st

spam = ['apples', 'bananas', 'tofu', 'cats','dogs','pigs']
conda(spam)
