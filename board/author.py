from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import logout_user, login_required, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from board.databaseorm import DB, Author


bp = Blueprint('author', __name__)


@bp.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('auth/profile.html')


@bp.route('/profile', methods=['POST'])
@login_required
def update_profile():
    current_user.firstname = request.form.get('first_name', current_user.firstname)
    current_user.lastname = request.form.get('last_name', current_user.lastname)
    current_user.email = request.form.get('email', current_user.email)

    new_password = request.form.get('password')
    if new_password:
        current_user.password = generate_password_hash(new_password, method='scrypt')

    DB.session.commit()

    flash('Profile updated!', category='success')

    return render_template('auth/profile.html')


@bp.route('/login', methods=['GET'])
def login():
    return render_template('auth/login.html')


@bp.route('/login', methods=['POST'])
def login_user_fn():
    email_input = request.form.get('email')
    password_input = request.form.get('password')

    user = DB.session.execute(
        DB.select(Author)
        .filter_by(email=email_input)
    ).scalar()

    if not user or not check_password_hash(user.password, password_input):
        flash('Password or email not match', category='error')
        return redirect(url_for('author.login'))
    else:
        login_user(user)
        flash('Logged in successfully', category='success')
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

    user = DB.session.execute(
            DB.select(Author)
            .filter_by(email=email_input)
    ).scalar()

    print(f'USER: {user}')

    if user is not None:
        flash('User already exists! Please login', category='error')
    else:
        # if user doesn't exist create and add to db
        user = Author(
            firstname=first_name,
            lastname=last_name,
            email=email_input,
            password=generate_password_hash(password_input, method='scrypt')
        )

        DB.session.add(user)
        DB.session.commit()
        flash('Account created successfully. Please login.', category='success')

    return redirect(url_for('author.login'))


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('pages.home'))