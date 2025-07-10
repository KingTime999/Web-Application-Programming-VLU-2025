from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '')
        return redirect(url_for('success', name=name))
    return render_template('name.html')

@app.route('/success/<name>')
def success(name):
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=5002)