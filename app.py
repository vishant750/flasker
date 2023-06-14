from flask import Flask,render_template

app=Flask(__name__)
favourite_pizza=['onion and capsicum','tomato','mushroom','veg loaded']
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
app.run(debug=True)