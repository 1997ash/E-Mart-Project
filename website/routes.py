from flask import redirect, render_template, request, url_for
from website import app
from website.models import Product
from website.form import SearchForm
# import jyserver.Flask as jsf

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
    if request.method == 'GET':
        keyword = request.args.get('query')
        # products = Product.query.filter(Product.description.like('%'+\
        #             keyword+'%'))
        if keyword == '衛生紙' or keyword == '舒潔':
            return redirect(url_for('result'))
        else:
            return render_template('notfound.html')

@app.route('/result ', methods=['GET'])
def result():
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(page=page, per_page=5)
    return render_template('result.html', products=products)
    # return App.render(render_template(''))

# # javascript
# @jsf.use(app)
# class App:
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count += 1
#         self.js.document.getElementById('').innerHTML = self.count