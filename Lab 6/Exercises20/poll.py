from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

votes = {
    "Cats": 0,
    "Dogs": 0,
    "Birds": 0
}

@app.route('/poll', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        option = request.form.get('option')
        if option in votes:
            votes[option] += 1
        return redirect(url_for('poll'))

    total_votes = sum(votes.values())
    percentages = {}

    for key, value in votes.items():
        if total_votes > 0:
            percentages[key] = round((value / total_votes) * 100, 1)
        else:
            percentages[key] = 0

    return render_template('poll.html', votes=votes, percentages=percentages, total=total_votes)

if __name__ == '__main__':
    app.run(debug=True, port=5019)
