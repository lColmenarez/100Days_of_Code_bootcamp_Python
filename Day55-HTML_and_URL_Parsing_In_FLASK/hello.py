from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return "<h1 style='text-align: center'>Hello World!</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/PxHEc3YRy3cfRuNBVE/giphy.gif' width=200>"

@app.route('/bye')
def bye():
    return "<u><em><b>Bye!</b></em></u>"

@app.route("/username/<path:name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} yerars old!"

if __name__ == '__main__':
    app.run(debug=True)