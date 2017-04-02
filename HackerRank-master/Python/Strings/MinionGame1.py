S = input()
p1_score = 0
p2_score = 0
for i in range(0,len(S)):
    if S[i] == "A" or S[i] == "E" or S[i] =="I" or S[i] == "O" or S[i] =="U":
        p1_score += len(S) - i
    else:
        p2_score += len(S) - i                
#p1_words = list(filter(None, p1_words))
#p2_words = list(filter(None, p2_words))
#l1=len(p1_words)
#l2=len(p2_words)
#if l1 > l2:
#    fin= p1_words
#    print('Kevin ' + str(l1))
#elif l1 < l2:
#    fin= p2_words
#    print('Stuart ' + str(l2))
if p1_score > p2_score:
    #fin= p1_words
    print('Kevin ' + str(p1_score))
elif p1_score < p2_score:
    #fin= p2_words
    print('Stuart ' + str(p2_score))
else:
    print('Draw')
