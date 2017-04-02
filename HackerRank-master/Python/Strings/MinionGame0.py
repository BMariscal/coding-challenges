S = input()
p1_words = []
p2_words = []
for i in range(0,len(S)):
    for j in range(i,len(S)+1):
        if S[i] == "A" or S[i] == "E" or S[i] =="I" or S[i] == "O" or S[i] =="U":
            print(S[i:j])
            p1_words.append(S[i:j])
        else:
            print(S[i:j])
            p2_words.append(S[i:j])
            
      
            
            
 
                    
p1_words = list(filter(None, p1_words))
p2_words = list(filter(None, p2_words))
l1=len(p1_words)
l2=len(p2_words)
if l1 > l2:
    fin= p1_words
    print('Kevin ' + str(l1))
elif l1 < l2:
    fin= p2_words
    print('Stuart ' + str(l2))
else:
    print('Draw')

# count ={}
# for character in fin:
#     count.setdefault(character,0)
#     count[character]= count[character]+1
# print(sum(count.values()))