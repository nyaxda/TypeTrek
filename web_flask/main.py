#!/usr/bin/python3
"""Main Module"""

from flask import Blueprint, render_template, session
from flask import redirect, url_for, request
from models.user import User
from models.exercise import Exercise
from models.base_model import session

main = Blueprint('main', __name__)


@main.route('/dashboard')
def dashboard():
    """dashboard route"""
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    user = session.query(User).get(user_id)
    return render_template('dashboard.html', user=user)


@main.route('/exercise<int:exercise_id>', methods=['GET', 'POST'])
def exercise(exercise_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    exercise = session.query(Exercise).get(exercise_id)
    if request.method == 'POST':
        # I need to add some code here for exercise submission
        pass
    return render_template('exercise.html', exercise=exercise)


@main.route('/report')
def report():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    user = session.query(User).get(user_id)
    # I need to add some code for report generation
    return render_template('report.html', user=user)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
