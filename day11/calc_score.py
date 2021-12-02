with open('scorelist.txt', 'r') as f :
    score = []
    for i in range(3):
        score.append(f.readline().split())
    #print(score)

    #총점 및 평균 계산
    for i in range(3):
        score[i][1] = int(score[i][1]) #인덱싱한 문자를 숫자로 변환
        score[i][2] = int(score[i][2])
        score.append(score[i][1]+score[i][2])

    print("***********성적표*************")
    print("=============================")
    print("이름 국어 수학 총점")
    print("=============================")
    for i in range(3):
        print("{} {} {} {}".format(score[i][0],score[i][1],score[i][2],score[i][3],score[i][4]))
    print()

    print("***********과목별 평균*************")
    sum_subj = [0,0] # 국어, 수학
    for i in range(3):
        sum_subj[0] += score[i][1] #국어 합계
        sum_subj[1] += score[i][2] #수학 합계

    print("국어 : %.2f 점, 수학 : %.2f 점" % (sum_subj[0]/3 , sum_subj[1]/3))