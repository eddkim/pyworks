import sqlite3

def getconn():
    con = sqlite3.connect("c:/pydb/mydb.db")
    return con

def select_emp(): #자료 검색
    conn = getconn()
    cur = conn.cursor() #db 작업 객체
    sql = 'SELECT * FROM employee ORDER BY emp_id' #db검색
    cur.execute(sql) #검색 실행
    rs = cur.fetchall() #모든 자료 가져오기
    #print(rs)
    for i in rs :
        print(i)
        conn.close() #db 연결 종료

def insert_emp(): #자료 삽입
    conn = getconn() #db 연결객체 생성
    cur = conn.cursor()  # db 작업 객체
    #입력 방법 1. 칼럼값을 직접 입력
    #sql = "INSERT INTO employee VALUES ('e1001','추신수',40,40000)" #db추가
    #방법 2. ? 기호 사용 - 동적입력 (뭐가 입력 될지 모름) ,이걸 더 많이 씀
    sql = "INSERT INTO employee VALUES (?,?,?,?)"
    cur.execute(sql,('e1005','박인비',33,30000))
    conn.commit() #커밋 실행 - 필수 (데이터에 변경이 생겼을때 반드시 명시)
    conn.close()

def selcet_one() : #특정 자료 검색
    conn= getconn()
    cur = conn.cursor()
    sql = "SELECT emp_id,name FROM employee WHERE emp_id = ?"
    cur.execute(sql,('e1002',))
    rs = cur.fetchone() #1명의 자료 반환
    print(rs)
    conn.close()

def update_emp(): #자료 수정
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE employee SET age=30 WHERE emp_id=?"
    cur.execute(sql,('e1004',))
    conn.commit()
    conn.close()

def delete_emp(): #자료 삭제
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE name = ?"
    cur.execute(sql,('안산',))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #insert_emp()
    #update_emp()
    #delete_emp()
    select_emp()  #select_emp()호출
    #selcet_one()