from flask import Flask, render_template, redirect, flash, request, session
import jinja2
import melons
from forms import LoginForm


app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined #for debugging, I guess?

app.secret_key = 'dev'

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
    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    cart[melon_id] = cart.get(melon_id, 0) + 1
    session.modified = True

    flash(f"Melon {melon_id} successfully added to cart")
    print(cart)
    return redirect('/cart')


@app.route("/cart")
def cart():
    cart_melons = []
    order_total = 0
    cart = session.get('cart', {})

    for melon_id, qty in cart.items():
        melon = melons.find_melon(melon_id)
        melon_total = qty * melon.price
        order_total += melon_total

        melon.quantity = qty
        melon.melon_total = melon_total
        cart_melons.append(melon)
        
    return render_template("cart.html", cart_melons=cart_melons, order_total=order_total)


@app.route('/empty-cart')
def empty_cart():
    session['cart'] = {}
    return redirect('/cart')

@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=5000, host="localhost")