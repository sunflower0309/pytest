li=[(1,'blue'), (3,'red'), (4,'blue'), (6,'yellow'), (9,'red')]

def colorsort(li):
    lired=[]
    liyellow=[]
    liblue=[]
    for i in range(len(li)-1):
        if li[i][1]=='red':
            lired.append(li[i])
        elif li[i][1]=='yellow':
            liyellow.append(li[i])
        elif li[i][1]=='blue':
            liblue.append(li[i])
    return lired+liblue+liyellow

def quicksortfindmid(k,index):#将整个序列分成key的两侧，左侧始终比key小，右侧始终比key大，递归到左右大小为1

    if k==[]:
        return
    else:
        key = k[0]
        left = []
        right = []
        for i in range(1, len(k)):
            if k[i] > key:
                right.append(k[i])
            else:
                left.append(k[i])
        left.append(key)
        print('index:',index)
        print('left:',left)
        print('right:',right,len(right))
        if len(right)==index-1:
            print(key)
            return key
        else:
            if index > len(right):
                quicksortfindmid(left, index-len(right))
            elif index < len(right):
                quicksortfindmid(right, index)
x=[1,4,3,5,6,9,8,3,12,54,67,98,345,2,7,13]
#[6,9,8,12,54,67,98,345,7]
print(quicksortfindmid(x,15))
