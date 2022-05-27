from flask import Flask 

app = Flask(__name__)

@app.route('/')

def coisa():
    return 'hellowwwwwwwwwwwwwwwww'

app.run()