#!/usr/bin/python3
"""Main Module"""

from flask import Blueprint, render_template, session
from flask import redirect, url_for, request
from models.user import User
from models.exercise import Exercise
from models.base_model import session
from flask import session as flask_session

main = Blueprint('main', __name__)


@main.route('/dashboard')
def dashboard():
    """dashboard route"""
    user_id = flask_session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    user = session.query(User).get(user_id)
    return render_template('dashboard.html', user=user)

@main.route('/exercises/<int:exercise_id>', methods=['GET'])
def exercise(exercise_id):
    user_id = flask_session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    exercise = session.query(Exercise).get(exercise_id)
    if not exercise:
        # Handle the case where no Exercise with the given exercise_id exists
        flash('No exercise found with the given ID.', 'error')
        return redirect(url_for('main.exercises'))
    user = session.query(User).get(user_id)
    return render_template('exercise_detail.html', exercise=exercise, user=user)

@main.route('/exercises', methods=['GET'])
def exercises():
    user_id = flask_session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    user = session.query(User).get(user_id)
    # Get difficulty from query parameters, default to 'all'
    difficulty_level = request.args.get('difficulty_level', 'all')
    if difficulty_level == 'all':
        exercises = session.query(Exercise).all()
    else:
        exercises = session.query(Exercise).filter_by(difficulty_level=difficulty_level).all()
    return render_template('exercises.html', exercises=exercises, difficulty_level=difficulty_level, user=user)

@main.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    user = session.query(User).get(user_id)
    # I need to add some code for report generation
    return render_template('report.html', user=user)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
