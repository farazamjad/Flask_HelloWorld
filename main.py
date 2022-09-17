
from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "HELLO WORLD FROM FARAZ"
if __name__ == "__main__":
    #app.run()
    app.run(port=3001,debug=True)
