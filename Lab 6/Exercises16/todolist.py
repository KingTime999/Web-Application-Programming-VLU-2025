from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Danh sách lưu công việc và trạng thái
tasks = []

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task_text = request.form.get('task')
        if task_text:
            tasks.append({"task": task_text, "completed": False})
        return redirect(url_for('todo'))

    return render_template('todolist.html', tasks=tasks)

@app.route('/toggle/<int:task_index>')
def toggle(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = not tasks[task_index]["completed"]
    return redirect(url_for('todo'))

if __name__ == '__main__':
    app.run(debug=True, port=5015)
