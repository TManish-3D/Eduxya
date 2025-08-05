from flask import Flask,render_template,request,flash,redirect,url_for
from form import Registration
app=Flask(__name__)
app.secret_key="loophole"
@app.route('/')
def home():
   return render_template("index.html")
@app.route('/register',methods=["POST","GET"])
def Register():
   form=Registration()
   if form.validate_on_submit():
     name=form.name.data
     email=form.email.data
     flash(f"Welcome! {name}")
     return render_template("success.html")
   return render_template("register.html",form=form)
@app.route('/success')
def success():
  return render_template('success.html')
   
   
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
    if not  message:
      flash("Empty input")
      return redirect(url_for("feedback"))
    flash("thank you")
    return "thank you"
   return render_template('feedback.html')
     
     
if __name__=="main":
   app.run(debug=True)
   
