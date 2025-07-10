from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def square():
    num = request.args.get('num')
    if num:
        try:
            n = int(num)
            result = n * n
            return render_template('answer.html', num=n, result=result)
        except ValueError:
            return render_template('math.html', error="Please enter a valid number.")
    return render_template('math.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)