from flask import Flask, render_template, request, flash

# Create a class for our APP
app = Flask(__name__)
app.secret_key = "una_password_random"


# Select route for the app
@app.route("/hello") #Sarà l'ultima parte dell'url

def index():
   flash("what's your name")
   return render_template("index.html")

@app.route("/greet",methods=["POST","GET"])
def greet():
   flash("Hi " + str(request.form['name_input']) + ", great to see you!")
   return render_template("index.html")
   





