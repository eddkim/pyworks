# 2차원 리스트

with open('animal.txt','w') as f :
    animal = ['dog','cat','cow','pig']

    #파일에 쓰기

    for i in animal :
        f.write(i+'\n')

#animal 텍스트 읽기
with open('animal.txt','r') as f :
    #animal = f.readline()
    #print(animal) 1차원 리스트

    #2차원 리스트

    animal = []
    for i in range(4):
        animal.append(f.readline().split())
    print(animal)