from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='template') #supplying template folder prarameter

JOBS = [
    {
        'id': 1,
        'title': 'Hi',
        'location': 'Selangor, Malaysia',
    },
    {
        'id': 2,
        'title': 'How are you',
        'location': 'Johor, Malaysia',
    }
]

@app.route("/")
def hello_world(): #define hello world
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)