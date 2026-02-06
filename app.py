from flask import Flask, render_template

app = Flask(__name__)

todos = ["Ät en banan", "Gör en girlang av papper", "Lär mig virka"]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)
if __name__ == '__main__':
    app.run(debug=True)
