import json
import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

DATA_FILE = 'todos.json'
def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return ["Va glad!", "Ät en banan", "Gör en girlang av papper"]

def save_todos(todos_list):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos_list, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    return render_template('index.html', todos=load_todos())

@app.route('/add', methods=['POST'])
def add():
    new_todo = request.form.get('todo', '').strip()
    if new_todo:
        todos_list = load_todos()
        todos_list.append(new_todo)
        save_todos(todos_list)
    
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_index>', methods=['POST'])
def delete(todo_index):
    todos_list = load_todos()
    if 0 <= todo_index < len(todos_list):
        del todos_list[todo_index]
        save_todos(todos_list)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5002)
