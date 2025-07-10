from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The best way to predict the future is to create it.",
    "Stay hungry, stay foolish. – Steve Jobs",
    "Life is what happens when you’re busy making other plans.",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
]

@app.route('/quote')
def quote():
    selected_quote = random.choice(quotes)
    return render_template('quote.html', quote=selected_quote)

if __name__ == '__main__':
    app.run(debug=True, port=5017)
