from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample initial tasks
tasks = ["Task 1", "Task 2", "Task 3"]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = request.form.get('new_task')
    tasks.append(new_task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
