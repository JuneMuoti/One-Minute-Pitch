from flask import render_template
from . import main
from flask_login import login_required,login_user,logout_user


@main.route('/')
def index():

    return render_template('index.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
