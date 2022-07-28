from flask import Flask, redirect, request, render_template, url_for


app = Flask(__name__)

# Your code should be below
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/product')
def pro():
    return render_template('product.html')

@app.route('/cart')
def car():
    return render_template('cart.html')
# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(port=1237, debug=True)
