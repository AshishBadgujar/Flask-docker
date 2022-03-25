from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return f'<p>Hello world, your ENV variable=<strong>{os.getenv("MY_ENV")}</strong></p>'

# main driver function
if __name__ == '__main__':
	app.run()