#웹 서버 만들기

from flask import Flask, render_template, request

app = Flask(__name__) #Flask 객체 app 생성

@app.route('/')  # @ - 애너테이션 ,'/' -  루트 경로, ip - 127.0.0.1 : 5000
def index():
    return render_template('index.html') #html 파일을 전송
    #return "<h1>Hello ~ Flask !!</h1>" #문자열을 페이지에 전송


@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST' :  #'POST' 방식이라면
        id = request.form['id']    #name 값을 가져옴
        pwd = request.form['passwd']
        name = request.form['name']
        return render_template('member_info.html', id = id,pwd = pwd, name = name)

    else:
        return render_template('register.html')

@app.route('/loop_index')
def get_loopindex():
    items = ['a','b','c','d']
    return render_template('loop_index.html',items=items)


app.run(debug=True)  # debug = True ,서비스 하기 전 개발 모드