from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Hello World ! <(`;`)> ! <|~.~|> !'

@app.route('/whereami')
def whereami():
    return 'Where am i? => \n Obviously far from home'

@app.route('/addition')
def addition():
    return 'i just felt like adding some more stuff'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
