# Sentiment Analysis System

This project is a Streamlit application that performs sentiment analysis on user-entered tweets. The application uses a trained machine learning model and vectorizer to predict the sentiment of the input tweet as "Negative," "Neutral," or "Positive."

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [License](#license)

## Requirements

- Python 3.6 or later
- Streamlit
- Scikit-learn
- Pandas

## Installation

To use the Sentiment Analysis System application, follow these steps:

1. Clone or download this repository.

2. Install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Place the trained model file (`updatedTrainedModel.sav`) and the fitted vectorizer file (`trained_count_vectorizer.pkl`) in the root directory of the project.

## Usage

To run the application:

1. Open a terminal or command prompt and navigate to the root directory of the project.

2. Run the Streamlit application:

    ```bash
    streamlit run sentiment_analysis_app.py
    ```

3. The application will open in a new tab in your default web browser.

4. Enter a tweet in the provided text area and click the "Detect Sentiment" button to see the sentiment prediction.

## File Descriptions

- `sentiment_analysis_app.py`: The main Streamlit application script for sentiment analysis.

- `updatedTrainedModel.sav`: The trained machine learning model file.

- `trained_count_vectorizer.pkl`: The fitted vectorizer file used to preprocess text data.

- `requirements.txt`: A file containing the list of required Python packages for the application.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as you wish. Please refer to the `LICENSE` file for more details.
