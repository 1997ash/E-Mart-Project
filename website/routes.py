from flask import redirect, render_template, request, url_for
from website import app
from website.models import Product
from website.form import SearchForm

@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=["GET","POST"])
def search():
    if request.method == 'POST':
        keyword = request.form['nm']
        form = SearchForm()
        products = Product.query
        ps = form.searched.data
        if form.validate_on_submit():
            products = products.filter(Product.description.like('%'+\
                        ps+'%'))
            products = Product.order_by(Product.price).all()
            return redirect(url_for('result', keyword=keyword))
    else:
        return render_template('notfound.html')

@app.route('/result ', methods=['GET'])
def result():
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(page=page, per_page=5)
    return render_template('result.html', products=products)