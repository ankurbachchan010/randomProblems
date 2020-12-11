
def canReach(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        print(True)
    elif x1>x2 or y1>y2:
        print(False)
    elif x1 == x2:
        bot(x1,x1+y1,x2,y2)
    else:
        bot(x1 + y1, y1, x2, y2)

canReach(2,2,4,6)