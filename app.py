from flask import Flask,render_template,request,jsonify
from function import checkpasswordstrength,generatepassword
app=Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/strengthcalculator",methods=['post'])
def strengthcalculator():
    return render_template('strengthcalci.html')

@app.route("/passwordscore",methods=['post'])
def showscore():
    data=request.form
    siu=data['password']
    score=checkpasswordstrength(siu)
    return render_template('score.html',god=score,jod=siu)

@app.route("/passwordgenerator",methods=['post'])
def generator():
    return render_template('generator.html')

@app.route("/generatedPassword",methods=['post'])
def showgenereatedpass():
    data=request.form
    siu=int(data['lengthofpass'])
    genpass=generatepassword(siu)
    return render_template('genpass.html',i=genpass)


if __name__=="__main__":
    app.run(debug=True)
