def avg(*ns):
    sum=0
    for n in ns:
        sum+=n
    return sum/len(ns)