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
print(longestWord(words))
