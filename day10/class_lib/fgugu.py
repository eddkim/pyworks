with open("99.txt",'a') as f :
    dan = 6
    for i in range(1,10):
        times = "%d x %d = %d\n" %(dan,i,dan*1)
        f.write(times)
        f.write('\n')