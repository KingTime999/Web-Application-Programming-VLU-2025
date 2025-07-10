from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert():
    result = None
    if request.method == 'POST':
        try:
            temp = float(request.form['temperature'])
            conversion_type = request.form['conversion']
            if conversion_type == 'CtoF':
                result = f"{temp}°C = {temp * 9 / 5 + 32:.2f}°F"
            elif conversion_type == 'FtoC':
                result = f"{temp}°F = {(temp - 32) * 5 / 9:.2f}°C"
            else:
                result = "Invalid conversion type."
        except ValueError:
            result = "Invalid temperature input."

    return render_template('temperature.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5010)
