def longestWord(words):
    words.sort(key=lambda x:[-len(x),x])
    for i in range(len(words)):
        for k in range(1,len(words)):
            if len(words[i])==1:
                return words[i]
            elif(len(words[k])+1==len(words[i])):
                temp = words[i].find(words[k])
                if temp != -1:
                    temp1=words[i]
                    signal = True
                    for t in range(1, len(temp1)):
                        if temp1[:-1] not in words:
                            signal = False
                            break
                        else:
                            temp1 = temp1[:-1]
                    if signal == True:
                        return words[i]
    return ''
words=["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]
# words.sort(key=lambda x:[-len(x),x])
# print(words)
#print(longestWord(words))
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 76')
    print('99 + 88 + 76 =', r)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
args = (1, 2, 3,4,5)
kw = {'d': 99, 'x': '#'}
f1(*args,**kw)

x1='man'
x2='woman'
x3='man'
print(hash(x1),hash(x2),hash(x3))
x=[2, 1, 2, 3, 4, 5, 3,3,3,3,4]
def findmaxfreq(k):
    dict={}
    for i in k:
        if str(i) in dict:
            dict[str(i)]=dict[str(i)]+1
        else:
            dict[str(i)]=1
    max=0
    maxkey=''
    for i in dict.keys():
        if dict[i]>max:
            max=dict[i]
            maxkey=i
    return maxkey
print(findmaxfreq(x))