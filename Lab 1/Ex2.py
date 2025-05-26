from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def student_info():
    student = {
        'name': 'Lê Tấn Nguyện',
        'student_id': '2374802010354', 
        'academic_year': '2024-2025',
        'major': 'Information Technology',
        'hobbies': ['Reading', 'Coding', 'Gaming'] 
    }
    return render_template('Ex2.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)