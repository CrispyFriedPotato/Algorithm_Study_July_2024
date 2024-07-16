from sys import stdin, stdout

n = stdin.readline().strip()
cards = stdin.readline().split()
dict_cards = {i:0 for i in cards}
for i in cards:
    dict_cards[i] +=1
    
m = stdin.readline().strip()
for i in stdin.readline().split():
    if i in dict_cards.keys():
        print(dict_cards[i], end=' ')
    else:
        print(0,end=' ')
    
    