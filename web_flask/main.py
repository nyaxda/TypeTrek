#!/usr/bin/python3
"""Main Module"""

from flask import Flask, Blueprint, render_template, session
from flask import redirect, url_for, request, flash, jsonify
from models.user import User
from models.exercise import Exercise
from models.progress import Progress
from models.base_model import session as db_session
from flask import session as flask_session


app = Flask(__name__)  # Create the Flask app
app.secret_key = 'supersecretkey'  # secret key

# set up the main blueprint
main = Blueprint('main', __name__)


@main.route('/dashboard')
def dashboard():
    """dashboard route"""
    user_id = flask_session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    user = db_session.query(User).get(user_id)

    # fetch average speed, accuracy and total exercises completed
    progress_records = db_session.query(Progress).filter_by(user_id=user_id).all()
    total_exercises = len(progress_records)
    if total_exercises > 0:
        avg_speed = sum(record.words_per_minute for record in progress_records) / total_exercises
        avg_accuracy = sum(record.accuracy for record in progress_records) / total_exercises
    else:
        avg_speed = 0
        avg_accuracy = 0
    return render_template('dashboard.html',
                           user=user, avg_speed=round(avg_speed, 2),
                           avg_accuracy=round(avg_accuracy, 2),
                           total_exercises=total_exercises)


@main.route('/exercises/<int:exercise_id>', methods=['GET'])
def exercise(exercise_id):
    """exercise route"""
    user_id = flask_session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    exercise = db_session.query(Exercise).get(exercise_id)
    if not exercise:
        # Handle the case where no Exercise with the given exercise_id exists
        flash('No exercise found with the given ID.', 'error')
        return redirect(url_for('main.exercises'))
    user = db_session.query(User).get(user_id)
    return render_template('exercise_detail.html',
                           exercise=exercise, user=user)


@main.route('/exercises', methods=['GET'])
def exercises():
    """exercises route"""
    user_id = flask_session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    user = db_session.query(User).get(user_id)
    # Get difficulty from query parameters, default to 'all'
    difficulty_level = request.args.get('difficulty_level', 'all')
    if difficulty_level == 'all':
        exercises = db_session.query(Exercise).all()
    else:
        exercises = db_session.query(Exercise).filter_by(
            difficulty_level=difficulty_level).all()
    return render_template('exercises.html', exercises=exercises,
                           difficulty_level=difficulty_level, user=user)


@main.route('/profile')
def profile():
    """profile route"""
    user_id = flask_session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    user = db_session.query(User).get(user_id)
    return render_template('profile.html', user=user)


@main.route('/save_progress', methods=['POST'])
def save_progress():
    """save progress route"""
    data = request.get_json()
    exercise_id = data.get('exercise_id')
    accuracy = data.get('accuracy')
    wpm = data.get('wpm')
    spm = data.get('spm')

    # Save progress to the database
    user_id = flask_session.get('user_id')
    if user_id and exercise_id:
        progress = Progress(
            user_id=user_id,
            exercise_id=exercise_id,
            accuracy=accuracy,
            words_per_minute=wpm,
            strokes_per_minute=spm
        )
        progress.save()
        return jsonify({
            'status': 'success',
            'message': 'Progress saved successfully'}), 200

    return jsonify({
        'status': 'error',
        'message': 'Failed to save progress'}), 400


@main.route('/next_exercise', methods=['GET'])
def next_exercise():
    """next exercise route"""
    current_exercise_id = request.args.get('current_exercise_id', type=int)
    difficulty_level = request.args.get('difficulty_level', type=str)

    # get the next exercise with the same difficulty level
    next_exercise = db_session.query(Exercise).filter(
        Exercise.id > current_exercise_id,
        Exercise.difficulty_level == difficulty_level
    ).order_by(Exercise.id).first()

    if next_exercise:
        return jsonify({'next_exercise_id': next_exercise.id}), 200
    else:
        return jsonify({'next_exercise_id': None}), 200


@main.route('/progress')
def progress():
    """progress route"""
    user_id = flask_session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))

    user = db_session.query(User).get(user_id)
    # Get all progress records for the user
    # .join is used to join the Exercise model to the Progress model
    progress_records = db_session.query(
        Progress).filter_by(user_id=user_id).join(Exercise).all()

    # Convert the progress records to a list of dictionaries
    progress_data = [record.to_dict() for record in progress_records]
    for record in progress_data:
        exercise = db_session.query(Exercise).get(record['exercise_id'])
        record['exercise_title'] = exercise.title

    return render_template('progress.html',
                           user=user, progress_records=progress_data)


@main.route('/change_password', methods=['POST'])
def change_password():
    """change password route"""
    try:
        data = request.get_json()
        user_id = flask_session.get('user_id')
        current_password = data.get('current_password')
        new_password = data.get('new_password')

        if not user_id:  # error 401 is for unauthorized access
            return jsonify({
                'status': 'error',
                'message': 'User not authenticated'}), 401

        user = db_session.query(User).get(user_id)

        # error 400 is for bad request
        if not user.check_password(current_password):
            return jsonify({
                'status': 'error',
                'message': 'Incorrect current password'}), 400

        # writing new password to the database
        user.set_password(new_password)
        user.save()

        # error 200 is for successful request
        return jsonify({
            'status': 'success',
            'message': 'Password changed successfully'}), 200
    except Exception as e:
        print(f"Error in change_password route: {e}")
        # error 500 is for internal server error
        return jsonify({
            'status': 'error',
            'message': f'An error occurred: {str(e)}'}), 500


# Register blueprint
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
