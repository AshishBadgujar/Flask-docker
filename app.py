from crypt import methods
from flask import Flask
from dotenv import load_dotenv
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'<p>Hello world, your ENV variable=<strong>{os.getenv("MY_ENV")}</strong></p>'

# main driver function
if __name__ == '__main__':
	app.run()