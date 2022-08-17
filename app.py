from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')
@app.route('/aboutus')
def aboutus():
  return render_template('aboutus.html')
@app.route('/minorproject')
def majorproject():
  return render_template('minorproject.html')
if __name__ == "__main__":
  app.run(debug=True)
