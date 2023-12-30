from flask import Flask,render_template,request,jsonify
from function import checkpasswordstrength,generatepassword,add_pass_to_db,load_pass_from_db,load_spass_from_db
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

@app.route("/storageVault",methods=['post'])
def vault():
    return render_template('vault.html')

@app.route("/storedata",methods=['post'])
def store():
    return render_template('storage.html')

@app.route("/stored",methods=['post'])
def storing():
    passdata=request.form
    add_pass_to_db(passdata)
    return render_template('saved.html',passdata=passdata)

@app.route("/extractdata",methods=['post'])
def extract():
    return render_template('extract.html')

@app.route("/extracted",methods=['post'])
def extracted():
    data=request.form
    pop=data['key']
    smoke=load_spass_from_db(pop)
    return render_template('extracted.html',la=smoke)


if __name__=="__main__":
    app.run(debug=True)
