#!/usr/bin/python3
"""
authentication module
"""
from flask import Blueprint, render_template
from flask import request, redirect, url_for, flash, session
from sqlalchemy.exc import SQLAlchemyError
from flask_login import logout_user

from models.user import User
from models.base_model import session
from flask import session as flask_session
from werkzeug.security import generate_password_hash, check_password_hash

# Blueprint is a way to organize a group of related views and other code.
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """login route"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = session.query(User).filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            flask_session['user_id'] = user.id
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check your username and password',
                  'danger')
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """register route"""
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            username = request.form.get('username')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')

            if password != confirm_password:
                flash('Passwords do not match')
                return render_template('register.html')
        
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(email=email, username=username,
                            password_hash=hashed_password)
            new_user.save()
            flash('Your account has been created!', 'success')
            return redirect(url_for('auth.login'))
        except SQLAlchemyError as e:
            session.rollback()
            print(str(e))
    return render_template('sign_up.html')

@auth.route('/logout')
def logout():
    if 'user_id' in flask_session:
        flask_session.pop('user_id')
    return redirect(url_for('auth.login'))

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
