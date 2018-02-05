from flask import render_template
from . import main
from flask_login import login_required,login_user,logout_user
from ..models import Category,Pitch


@main.route('/')
def index():
    title = 'Home'

    categories = Category.get_categories()

    return render_template('index.html' ,title=title, categories=categories)

@main.route('/category/new',methods=['GET','POST'])
@login_required
def new_category():
    form= CategoryForm()
    if form.validate_0n_submit():
        name=form.name.data
        new_category=Category(name=name)
        new_category.save_category()
        return redirect(url_for('.index'))
    title= 'New Category'
    return render_template('new_category.html',category_form=form)


