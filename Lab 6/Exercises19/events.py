from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

events = []

@app.route('/events', methods=['GET', 'POST'])
def event_list():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        if name and date:
            events.append({'name': name, 'date': date})
        return redirect(url_for('event_list'))
    return render_template('events.html', events=events)

if __name__ == '__main__':
    app.run(debug=True, port=5018)
