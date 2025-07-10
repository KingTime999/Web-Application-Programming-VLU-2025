from flask import Flask, render_template, abort

app = Flask(__name__)

menu_data = {
    "food": [
        {"name": "Burger", "price": 5},
        {"name": "Pizza", "price": 8},
        {"name": "Pasta", "price": 6}
    ],
    "drinks": [
        {"name": "Coffee", "price": 2},
        {"name": "Tea", "price": 1.5},
        {"name": "Juice", "price": 3}
    ]
}

@app.route('/menu/<category>')
def menu(category):
    items = menu_data.get(category)
    if not items:
        return "Category not found", 404
    return render_template('menu.html', category=category.title(), items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5016)
