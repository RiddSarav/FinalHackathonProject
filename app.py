from module import SymptomCheck
from flask import Flask
from flask import *
app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return render_template('index2.html')
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        gender = request.form.get('gender')
        birth = int(request.form.get('age'))
        number=request.form.get('symptomnumber')
        try:
            r= SymptomCheck(birth,number,gender)
            return render_template('result.html',r=r)
        except IndexError:
            return "your symptom range goes not let us get any illness for those symptoms please imput additional symptoms or consult a medical professional"
    return render_template('hackathonstuff.html')
@app.route("/about")
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
if __name__ == '__main__':
    app.run()
