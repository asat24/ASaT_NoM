lst=[["-","A","O","B"]
,["A",1,2,3]
,["O",2,1,4]
,["B",3,4,1]]

n=len(lst)

for i in range(n):
    print(lst[i])

def load(r,c,v):
    global lst
    if r==c:
        lst[r][c]=v
    else:
        lst[r][c]=v
        lst[c][r]=v

load(1,3,7)

# r=1
# c=1
# v=7

# lst[r][c]=v

for i in range(n):
    print(lst[i])