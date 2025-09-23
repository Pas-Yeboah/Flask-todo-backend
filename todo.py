from flask import Flask

app = Flask(__name__) 
todos = ["cook", 'drink' ,'sleep' ,'code']

@app.route('/')
def get_all_items():
    return todos
@app.route('/first_item')
def first_item():
    return todos[0]
@app.route('/last_item')
def last_item():
    return todos[-1]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')