from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
<<<<<<< HEAD
    return "Halló heimur!"
=======
    return "Halló frá hotfix"
>>>>>>> hotfix

if __name__ == "__main__":
    app.run(debug=True)
