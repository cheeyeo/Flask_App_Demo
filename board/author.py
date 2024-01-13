from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import logout_user, login_required, login_user
from werkzeug.security import check_password_hash, generate_password_hash
from board.databaseorm import db
from board.databaseorm import Author


bp = Blueprint('author', __name__)


@bp.route('/login', methods=['GET'])
def login():
    return render_template('auth/login.html')


@bp.route('/login', methods=['POST'])
def login_user_fn():
    email_input = request.form.get('email')
    password_input = request.form.get('password')

    user = db.session.execute(
        db.select(Author)
        .filter_by(email=email_input)
    ).scalar_one()

    if not user or not check_password_hash(user.password, password_input):
        flash('Password or email not match')
        return redirect(url_for('author.login'))
    else:
        login_user(user)
        return redirect(url_for('pages.home'))


@bp.route('/signup', methods=['GET'])
def signup():
    return render_template('auth/register.html')


@bp.route('/signup', methods=['POST'])
def signup_user():
    email_input = request.form.get('email')
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    password_input = request.form.get('password')

    try:
        user = db.session.execute(
            db.select(Author)
            .filter_by(email=email_input)
        ).scalar_one()
    except Exception as e:
        print(e, type(e))
        user = None


    print(f'USER: {user}')

    if user is not None:
        flash('User already exists! Please login')
    else:
        # if user doesn't exist create and add to db
        user = Author(
            firstname=first_name,
            lastname=last_name,
            email=email_input,
            password=generate_password_hash(password_input, method='scrypt')
        )

        db.session.add(user)
        db.session.commit()

    return redirect(url_for('author.login'))


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('pages.home'))