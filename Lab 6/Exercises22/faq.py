from flask import Flask, render_template

app = Flask(__name__)


faqs = {
    1: {"question": "What is Flask?", "answer": "Flask is a lightweight web framework for Python."},
    2: {"question": "What is Jinja2?", "answer": "Jinja2 is a template engine used with Flask."},
    3: {"question": "How to run a Flask app?", "answer": "Use 'python filename.py' and open the localhost URL."}
}

@app.route('/faq/<int:question_id>')
def show_faq(question_id):
    faq = faqs.get(question_id)
    if not faq:
        return "FAQ not found", 404
    return render_template('faq.html', faq=faq)

if __name__ == '__main__':
    app.run(debug=True, port=5021)
