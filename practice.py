from flask import Flask, render_template,request
app = Flask(__name__)

#survey questions
question ="What is your favorite food?"

@app.route('/')
def index(): return render_template('survey.html', question=question)

@app.route('/submit',methods=['POST'])
def submit():
    answer = request.form.get('answer')
    return render_template('thank_you.html', answer=answer)

if __name__=='__main__':
    app.run(debug=True)