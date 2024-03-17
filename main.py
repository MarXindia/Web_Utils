from flask import Flask, request ,  render_template

app = Flask(__name__)

@app.route('/Index')
def hello():
    return "<p> Hello World </p>"


app.run()