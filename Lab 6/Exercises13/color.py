from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/color', methods=['GET', 'POST'])
def set_color():
    background_color = "white"
    if request.method == 'POST':
        color_input = request.form.get('color')
        if color_input:
            background_color = color_input
    return render_template('color.html', color=background_color)

if __name__ == '__main__':
    app.run(debug=True, port=5012)
