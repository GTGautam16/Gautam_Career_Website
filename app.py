from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'ID': 1,
        'title': 'Software Engineer',
        'Location' : 'Mumbai, Maharashtra, India',
        'Salary' : '₹15,00,000'
    },
    {
        'ID': 2,
        'title': 'Backend Engineer',
        'Location' : 'Thane, Maharashtra, India',
        'Salary' : '₹12,00,000'
    },
    {
        'ID': 3,
        'title': 'Frontend Engineer',
        'Location' : 'Pune, Maharashtra, India',
    },
    {
        'ID': 4,
        'title': 'UI/UX Designer',
        'Location' : 'San Francisco, USA',
        'Salary' : '$1,500,'
    }
]   


@app.route("/")
def Greet():
    return render_template("home.html", jobs=JOBS, company_name='Gautam')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)