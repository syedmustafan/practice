st = "abcde"
def countMin(st):
    right = len(st) - 1
    left = 0
    palin = 0
    for _ in range(len(st)//2):
        if st[left] == st[right]:
            left += 1
            right -= 1
            palin += 1

        else:
            pass
    if palin == len(st)//2:
        print(0)
    else:    
        xx = st[1:]
        store = xx[::-1]
        answer = store + st
        print(len(store))    
countMin(st)