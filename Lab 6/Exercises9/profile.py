from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    is_admin = (username.lower() == 'admin')
    return render_template('profile.html', username=username, is_admin=is_admin)

if __name__ == '__main__':
    app.run(debug=True, port=5008)
