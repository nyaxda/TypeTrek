#!/usr/bin/python3
"""
authentication module
"""
from flask import Blueprint, render_template
from flask import request, redirect, url_for, flash, session

from models.user import User
from models.base_model import session
from werkzeug.security import generate_password_hash, check_password_hash

# Blueprint is a way to organize a group of related views and other code.
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """login route"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = session.query(User).filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login Unsuccessful. Please check your email and password',
                  'danger')
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """register route"""
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, username=username,
                        password=hashed_password)
        session.add(new_user)
        session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('sign_up.html')

@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
