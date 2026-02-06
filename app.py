from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

todos = ["Va glad!", "Ät en banan", "Gör en girlang av papper", "Lär dig virka"]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    new_todo = request.form['todo']
    if new_todo:
        todos.append(new_todo)
    
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_index>', methods=['POST'])
def delete(todo_index):
    if 0 <= todo_index < len(todos):
        del todos[todo_index]
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5002)
