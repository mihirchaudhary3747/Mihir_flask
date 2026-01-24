from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('about.html')
@app.route('/motivation')
def mtv():
  return render_template('motivation.html')
@app.route("/resume")
def resumepd():
  return render_template('resume.hmtl')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
