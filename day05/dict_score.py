#학생 성적 합계 및 평균

student = [
    {'name':'김하나', 'kor':80, 'math':70, 'eng':90},
    {'name':'김이둘', 'kor':60, 'math':80, 'eng':50},
    {'name':'김박셋', 'kor':90, 'math':90, 'eng':100}
]

print("이름   총점  평균")
for s in student:
    sum_v = s['kor']+s['math']+s['eng']
    avg = sum_v/3
    print("%s %d %.1f"%(s['name'],sum_v,avg))
print()

#총점과 평균

sum_kor=0
sum_math=0
sum_eng=0

for s in student:
    sum_kor+=s['kor']
    sum_math += s['math']
    sum_eng+=s['eng']

avg_kor = sum_kor/3
avg_math = sum_math/3
avg_eng = sum_eng/3


print("국어 합계 : %d"%sum_kor)
print("수학 합계 : %d"%sum_math)
print("영어 합계 : %d"%sum_eng)
print("국어 평균 : %d"%avg_kor)
print("수학 평균 : %d"%avg_math)
print("영어 평균 : %d"%avg_eng)