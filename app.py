from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
app=Flask(__name__)
app.config['SECRET_KEY'] = "my key"
favourite_pizza=['onion and capsicum','tomato','mushroom','veg loaded']

#Create a form class
class former(FlaskForm):
    name=StringField("What's your name",validators=[DataRequired()])
    submit=SubmitField("Submit")
@app.route("/")
def home():
    return render_template("index.html",favourite_pizza=favourite_pizza)
#filter that can be used safe,capitalize,lower,upper,title,trim,striptags, all of these are jinga filters.
#We can also use if-else and for loop using jenga template.
@app.route('/about/<user>')
def about(user):
    return"<h3>Hello{}".format(user)
#Error page create in flask
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"), 500
#Creating route for form
@app.route("/name",methods=['GET','POST'])
def name():
    name = None
    form = former()
    #Validate Form
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template('name.html',name=name,form=form)


app.run(debug=True)