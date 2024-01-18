from flask import Flask, render_template, request

app = Flask(__name__)

# List to store tasks
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('index.html', tasks=tasks)

@app.route('/remove/<task_index>')
def remove_task(task_index):
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(tasks):
            del tasks[task_index - 1]
    except ValueError:
        pass  # Ignore if the task_index is not a valid integer

    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
