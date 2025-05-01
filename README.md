# AI-Based Career Counseling System 🎓🤖

An AI-driven career counseling platform designed to assist secondary school students in making informed career decisions through interactive gamified IQ assessment, machine learning predictions, and chatbot-based guidance.

## 🧠 Overview

This project presents an innovative approach to personalized career counseling using Artificial Intelligence. It combines a game-based IQ assessment module, a machine learning-based prediction engine (Random Forest), and an AI chatbot to provide tailored career guidance. The system is especially useful for educational institutions with limited access to human counselors.

## 📌 Features

- 🎮 **Aptitude Game**: Engaging cognitive games to evaluate memory, logic, math skills, spatial awareness, and reasoning.
- 🌲 **Random Forest Model**: Predicts career paths based on IQ scores and historical data.
- 💬 **AI Chatbot**: Provides real-time, multilingual, and personalized career guidance.
- 📊 **Accurate Prediction**: Achieved 95.50% accuracy in pilot testing.
- 🔒 **Data Privacy**: Designed with strict privacy controls.

## 🏗️ System Architecture

1. **User Registration**: Student enters basic info.
2. **Game Module**: Plays aptitude game to evaluate cognitive profile.
3. **IQ Classification**: Scores normalized and classified into Low, Average, or High.
4. **Career Prediction**: Random Forest model suggests suitable paths.
5. **Chatbot Guidance**: Student interacts with chatbot for detailed advice.

## 📈 Model Details

- **Algorithm**: Random Forest
- **Training Data**: Includes IQ scores, academic performance, and career outcomes
- **Evaluation**: 95.50% accuracy via cross-validation

## 💡 Theory Behind It

### IQ Scoring

The aptitude game uses weighted scoring based on task difficulty and normalizes scores using z-scores:

```
Total Score = ∑(wi * si)
Normalized Score = (Score - μ) / σ
```

IQ Categories:
- Low: < -1 SD
- Average: -1 to +1 SD
- High: > +1 SD

### Random Forest

- Aggregates predictions from multiple decision trees
- Handles high-dimensional data efficiently
- Reduces bias and overfitting

## 📷 Screenshots



## 🔮 Future Scope

- Adaptive difficulty levels in the game
- More career paths and datasets
- Integration of additional ML models (e.g., XGBoost, Neural Nets)

## 👩‍💻 Team

- Mrs. Y Ashwini – Assistant Professor, CSE Dept., Anurag University
- P. Shanmukhapriya Sravani – Student
- U. Swapnika – Student
- B. Vyshnavi – Student

## 📚 References

- Talib et al., 2023 – AI Career Guidance in Morocco
- Gunje et al., 2024 – AI-based Career Counseling System
- Borchert, 2002 – Career Choice Factors of High School Students

## 📜 License

This project is developed for academic and research purposes. Contact the corresponding authors for reuse and deployment permissions.

## 📬 Contact

For queries or collaboration:
📧 ashwini.cse@anurag.edu.in
