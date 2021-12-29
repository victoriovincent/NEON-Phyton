from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():    
#     return 'Hello, World!'

@app.route('/<page_name>')
def hello_world(page_name):
    html = '<h1> Hello World! </h1>'
    html += '<h2> This is {} page </h2>' .format(page_name)     
    return html

@app.route('/home')
def hello():
    return 'Hello, home'

if __name__ == '__main__':    
    app.run()