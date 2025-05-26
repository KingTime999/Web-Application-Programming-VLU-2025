from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        gender = request.form.get('gender')
        membership = request.form.get('membership')
        color = request.form.get('favcolor')
        correct = request.form.get('correct')

      
        return f"Submitted: {username}, {gender}, {membership}, {color}, Correct: {correct}"

    return render_template('Ex3.html')

if __name__ == '__main__':
    app.run(debug=True , port=5002)
