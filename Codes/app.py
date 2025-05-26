from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained regression model
model = joblib.load('random_forest_regressor_iq.pkl')

# Load the dataset for career paths and recommended courses
data = pd.read_csv('Dataset/iq_occupation_dataset.csv')

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/quiz')
def quiz():
    return render_template('game.html')

@app.route('/result')
def result():
    # Get the quiz score from the query parameters
    quiz_score = int(request.args.get('iqScore', 0))  # This is the raw score
    quiz_percentage = (quiz_score / 36) * 100  # Convert to percentage

    # Prepare input features for the model
    input_features = np.array([[quiz_percentage]])  # Create a 2D array for model input

    # Use the model to predict the IQ score
    iq_score = model.predict(input_features)[0]  # Get the predicted IQ score

    # Retrieve career path and recommended courses based on predicted IQ score
    career_path, recommended_courses = get_career_path_and_courses(iq_score)

    return render_template('result.html', iq_score=int(iq_score), career=career_path, courses=recommended_courses)

def get_career_path_and_courses(iq_score):
    """Function to retrieve career path and recommended courses based on IQ Score."""
    # Find the row closest to the predicted IQ Score
    closest_idx = (data['IQ Score'] - iq_score).abs().idxmin()
    predicted_row = data.iloc[closest_idx]
    career_path = predicted_row['Career Path']
    recommended_courses = predicted_row['Recommended Courses']
    return career_path, recommended_courses

if __name__ == '__main__':
    app.run(debug=True)
