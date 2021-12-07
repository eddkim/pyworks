# book 테이블 만들기
import sqlite3

def getconn():
    con=sqlite3.connect('./output/sample.db')
    return con

def create_table() :
    conn = getconn()
    cur = conn.cursor()
    sql = """
    CREATE TABLE book(
        book_no INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        publisher TEXT NOT NULL,
        page INTEGER
    )    
    """

    #AUTOINCREMENT - 자동순번 (sequence)
    cur.execute(sql)
    conn.commit()
    print("book 테이블 생성")
    conn.close()

def insert_book():
    conn=getconn()
    cur=conn.cursor()
    sql = "INSERT INTO book(title,publisher,page) VALUES " \
          "(?,?,?)"
    cur.execute(sql,('점프 투 파이썬','박응용',300))
    conn.commit()
    conn.close()

def select_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM book"
    cur.execute(sql)
    rs = cur.fetchall() # 리스트로 반환
    #print(rs)
    for i in rs :
        print(i)
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"
    cur.execute(sql,(1,))
    rs = cur.fetchone()
    print(rs)
    conn.close()

def update_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE book set page = ? WHERE book_no = ?"
    cur.execute(sql,(300,2))
    conn.commit()
    conn.close()

def delete_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM book WHERE book_no = ?"
    cur.execute(sql,(1,))
    conn.commit()
    conn.close()


if __name__ == "__main__" :
    #create_table()
    #insert_book()
    update_book()
    #delete_book()
    select_book()
    #select_one()
