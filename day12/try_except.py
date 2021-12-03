#try ~ except ~ else
#에러가 없으면 try ~ else
#에러가 있으면 try ~ except

try :
    with open('2021kbo.txt','r') as f :
        team = f.readlines()
    print("1번")
except :
    print("2번")
else :
    for i in team :
        print(i,end='')
