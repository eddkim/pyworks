setInterval(myWatch, 1000)

function myWatch(){
    var date = new Date(); //날짜,시간 객체 생성
    var now = date.toLocaleTimeString(); //시간 출력 객체 생성
    document.getElementById('display').innerHTML = now
}