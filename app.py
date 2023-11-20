from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample initial tasks
tasks = [{'name': 'Task 1', 'completed': False}, {'name': 'Task 2', 'completed': False},
         {'name': 'Task 3', 'completed': False}]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task_name = request.form.get('new_task')
    new_task = {'name': new_task_name, 'completed': False}
    tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    del tasks[task_id - 1]
    return redirect(url_for('index'))

@app.route('/toggle_task/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    tasks[task_id - 1]['completed'] = not tasks[task_id - 1]['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
