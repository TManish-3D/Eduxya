from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def home():
   return render_template("index.html")
@app.route('/Entrance',methods=["POST","GET"])
def Entrance():
   if request.method=="POST":
    message=request.form.get("message")
    return "Thank you!"
   return render_template("next.html")

   
@app.route('/feedback',methods=["POST","GET"])
def feedback():
   if request.method=="POST":
    message=request.form.get("message")
    return render_template("index.html")
   return render_template('feedback.html')
     
     
if __name__=="main":
   app.run(debug=True)
   
