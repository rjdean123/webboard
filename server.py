from flask import Flask
app = Flask(__name__)

count = 0

@app.route("/")
def hello():
    return "visitor # " + str(count)
    count+=1

if __name__ == "__main__":
    app.run()
