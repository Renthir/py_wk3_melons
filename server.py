from flask import Flask, render_template, redirect, flash, request
import jinja2
import melons


app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined #for debugging, I guess?

#routes
@app.route("/")
def homepage():
    return render_template("base.html")

@app.route("/melons")
def all_melons():
    melon_list = melons.get_melons()
    return render_template("melons.html", melon_list=melon_list)

@app.route("/melon/<melon_id>")
def melon_details(melon_id):
    melon = melons.find_melon(melon_id)
    return render_template("melon_details.html", melon=melon)

@app.route("/add_to_cart<melon_id>")
def add_to_cart(melon_id):
    return f"{melon_id} added to card"

@app.route("/cart")
def cart():
    return render_template("cart.html")


if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=5000, host="localhost")