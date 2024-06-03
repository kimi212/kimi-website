from flask import Flask, render_template

app = Flask(__name__, template_folder='template') #supplying template folder prarameter

@app.route("/")
def hello_world(): #define hello world
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)