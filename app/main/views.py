from flask import render_template
from . import main
from flask_login import login_required,login_user,logout_user
from ..models import Category


@main.route('/')
def index():
    title = 'Home'

    categories = Category.get_categories()

    return render_template('index.html' ,title=title, categories=categories)




