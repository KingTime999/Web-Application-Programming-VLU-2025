from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

entries = []

@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        if name and message:
            entries.append({'name': name, 'message': message})
        return redirect(url_for('guestbook'))
    return render_template('guestbook.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True, port=5013)
