import random as r
with open("word.txt",'w') as f :
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'strawberry', 'grape', 'garlic', 'onion', 'potato','smile']

    for w in word:
        f.write(w + ' ')

#단어를 랜덤하게 추출하기

with open ('word.txt','r') as f:
    #word = f.readlines() #리스트로 반환 됨
    word=f.readline().split()
    w = r.choice(word)
    print(w)