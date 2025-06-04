from flask import Flask, render_template, request
import csv
from datetime import datetime

app = Flask(__name__)

#반 와이파이
allowed_ips = [
    '192.168.1.14',
    '192.168.1.31',
    '192.168.1.128',
    '192.168.1.130',
    '192.168.1.136'
]

@app.route('/')
def show_attendance_page():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def check_attendance():
    student_number = request.form['student_id']  # 학번 받아오기
    my_ip = request.remote_addr  # 접속한 내 IP
    now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 현재 시간

    # 와이파이 ip 맞다면 출석 인정
    if my_ip in allowed_ips:
        with open('attendance.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_number, my_ip, now_time])
        return f'출석 완료!<br>학번: {student_number}<br>IP: {my_ip}'
    else:
        return f'출석 실패: 학교 와이파이가 아님<br>당신의 IP: {my_ip}'

if __name__ == '__main__':
    app.run(debug=True)