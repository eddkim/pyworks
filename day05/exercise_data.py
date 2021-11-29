#1

Kor = 80; Eng = 75; Math = 55;
avg = (Kor+Eng+Math)/3
print(avg)

#2
a = 13
if a % 1 :
    print("홀수입니다.")
else : print("자연수입니다")

#3
pin = "881120-1068234"
yyyymmdd = pin[0:6];num = pin[7:14]
print("생년월일 : ",yyyymmdd);print("뒷부분 : ",num)

#4
if pin[7] == 1 or 3 :
    print("남자입니다.")
elif pin[7] == 2 or 4 :
    print("여자입니다.")
else : print("오류")

#5
a = "a:b:c:d"
b = a.replace(':','#')
print(b)

#6
a = [1,3,5,4,2]
a.sort();print(a)
a.reverse();print(a)

#7

a=['Life','is','too','short']
result = ' '.join(a);print(result)

#8
a = (1,2,3)
a = a+(4,)
print(a)

#9


#10
a={'A':90, 'B':80, 'C':70}
result= a.pop('B')
print(a);print(result)
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a);b=list(a)

