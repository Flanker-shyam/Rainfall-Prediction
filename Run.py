import streamlit as st
import numpy as np
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler

# Placeholder function for predicting rainfall (replace with your model)
def predict_rainfall(features):
    """
    Predicts the amount of rainfall based on the given features.

    Args:
        features (pandas.DataFrame): A DataFrame containing the features used for prediction.

    Returns:
        numpy.ndarray: An array of predicted rainfall values.
    """
    
  # The line `features['Events'] = features['Events'].apply(lambda x: ','.join(x) if isinstance(x,
  # list) else x)` is converting the 'Events' column in the features DataFrame from a list of events
  # to a comma-separated string of events.
    features['Events'] = features['Events'].apply(lambda x: ','.join(x) if isinstance(x, list) else x)

    # The code `encoder = LabelEncoder()` creates an instance of the `LabelEncoder` class, which is
    # used to encode categorical variables into numerical values.
    encoder = LabelEncoder()
    features['Events'] = encoder.fit_transform(features['Events'])

    # The code `sc = StandardScaler()` creates an instance of the `StandardScaler` class, which is
    # used to standardize the features by removing the mean and scaling to unit variance.
    sc = StandardScaler()
    x_std = sc.fit_transform(features)
    x_std = pd.DataFrame(x_std, columns=features.columns)

    # The line `model = joblib.load('model_new.pkl')` is loading a machine learning model from a file
    # called 'model_new.pkl'. The model is stored in the file using the joblib library's `dump`
    # function. By loading the model, we can use it to make predictions on new data.
    model = joblib.load('model_new.pkl')

    # `rainfall = model.predict(x_std)` is using the trained machine learning model to make
    # predictions on the standardized input features (`x_std`). The `predict` method takes the
    # standardized features as input and returns an array of predicted rainfall values. These
    # predicted values represent the amount of rainfall that is estimated based on the given weather
    # conditions.
    rainfall = model.predict(x_std)
    return rainfall

import streamlit as st
import pandas as pd

def main():
    """
    This function creates a Streamlit app for predicting rainfall based on weather conditions.
    It allows the user to input various weather parameters such as temperature, humidity, pressure, wind, etc.
    The app then uses a machine learning model to predict the amount of rainfall based on the input parameters.
    """

    # The `st.set_page_config()` function is used to customize the appearance and layout of the
    # Streamlit app page title and favicon
    st.set_page_config(
        page_title="Rainfall Prediction App",
        page_icon=":umbrella:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # The `st.markdown()` function is used to display formatted text in Streamlit. In this case, it is
    # used to apply custom CSS styles to the app's elements. The CSS styles are defined within the
    # `<style>` tags and include styles for the body, header, description, usage, and button elements.
    # The `unsafe_allow_html=True` argument allows the HTML code within the `st.markdown()` function
    # to be rendered as HTML.
    st.markdown(
        """
        <style>
            body {
               
                background-color: #87CEEB;
                font-family: 'Arial', sans-serif;
            }
            .header {
                color: #1f4e79;
                font-size: 3em;
                padding: 20px;
                text-align: center;
                font-weight: bold;
            }
            .description {
                color: #333;
                font-size: 1.5em;
                padding: 20px;
                text-align: center;
            }
            .usage {
                color: #1f4e79;
                font-size: 2em;
                font-weight: bold;
                padding: 10px;
            }
            .button {
                background-color: #1f4e79;
                color: white;
                font-size: 1.5em;
                padding: 15px 30px;
                border-radius: 8px;
                margin-top: 20px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .button:hover {
                background-color: #15335e;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


    # The line `st.markdown("<div class='header'>Rainfall Prediction App</div>",
    # unsafe_allow_html=True)` is used to display a header in the Streamlit app.
    st.markdown("<div class='header'>Rainfall Prediction App</div>", unsafe_allow_html=True)

   # The line `st.markdown("<div class='description'>Predict rainfall based on weather
   # conditions.</div>", unsafe_allow_html=True)` is used to display a description of the app in the
   # Streamlit interface.
    st.markdown("<div class='description'>Predict rainfall based on weather conditions.</div>", unsafe_allow_html=True)

   # The code block you provided is creating sliders in the Streamlit app interface for the user to
   # input values for various weather parameters such as temperature, dew point, humidity, sea level
   # pressure, visibility, and wind speed.
    TempHighF = st.slider("Temperature High (F)", min_value=0, max_value=100, value=50)
    TempAvgF = st.slider("Temperature Avg (F)", min_value=0, max_value=100, value=25)
    TempLowF = st.slider("Temperature Low (F)", min_value=0, max_value=100, value=10)
    DewPointHighF = st.slider("Dew Point High (F)", min_value=0, max_value=100, value=30)
    DewPointAvgF = st.slider("Dew Point Avg (F)", min_value=0, max_value=100, value=15)
    DewPointLowF = st.slider("Dew Point Low (F)", min_value=0, max_value=100, value=5)
    HumidityHighPercent = st.slider("Humidity High (%)", min_value=0, max_value=100, value=80)
    HumidityAvgPercent = st.slider("Humidity Avg (%)", min_value=0, max_value=100, value=50)
    HumidityLowPercent = st.slider("Humidity Low (%)", min_value=0, max_value=100, value=20)
    SeaLevelPressureHighInches = st.slider("Sea Level Pressure High (inches)", min_value=28, max_value=31, value=30)
    SeaLevelPressureAvgInches = st.slider("Sea Level Pressure Avg (inches)", min_value=28, max_value=31, value=29)
    SeaLevelPressureLowInches = st.slider("Sea Level Pressure Low (inches)", min_value=28, max_value=31, value=28)
    VisibilityHighMiles = st.slider("Visibility High (Miles)", min_value=0, max_value=10, value=8)
    VisibilityAvgMiles = st.slider("Visibility Avg (Miles)", min_value=0, max_value=10, value=5)
    VisibilityLowMiles = st.slider("Visibility Low (Miles)", min_value=0, max_value=10, value=2)
    WindHighMPH = st.slider("Wind High (MPH)", min_value=0, max_value=50, value=20)
    WindAvgMPH = st.slider("Wind Avg (MPH)", min_value=0, max_value=50, value=10)
    WindGustMPH = st.slider("Wind Gust (MPH)", min_value=0, max_value=50, value=15)

   # The code `events_options = ["Rain", "Snow", "Thunderstorm", "Wind", "Fog"]` creates a list of
   # options for the user to select from for the "Events" feature. The options include different types
   # of weather events such as rain, snow, thunderstorm, wind, and fog.
    events_options = ["Rain", "Snow", "Thunderstorm", "Wind", "Fog"]
    selected_events = st.multiselect("Select Events", events_options)

    # The code `day = st.slider("Day", min_value=1, max_value=31, value=15)` creates a slider in the
    # Streamlit app interface for the user to select a day of the month. The slider has a minimum
    # value of 1, a maximum value of 31, and a default value of 15.
    day = st.slider("Day", min_value=1, max_value=31, value=15)
    month = st.slider("Month", min_value=1, max_value=12, value=6)
    year = st.slider("Year", min_value=2000, max_value=2023, value=2022)

    # The line `if st.button("Predict Rainfall"):` is checking if the "Predict Rainfall" button in the
    # Streamlit app interface has been clicked. If the button is clicked, the code block inside the if
    # statement will be executed. This allows the app to trigger the prediction of rainfall based on
    # the selected weather parameters when the button is clicked.
    if st.button("Predict Rainfall"):

       # The `data` dictionary is used to store the values of various weather parameters and other
       # features that are used for predicting rainfall. Each key in the dictionary represents a
       # specific feature, such as temperature, humidity, pressure, wind, etc., and the corresponding
       # value represents the user-selected value for that feature in the Streamlit app interface. The
       # dictionary is then used to create a DataFrame, `features_df`, which is passed to the
       # `predict_rainfall` function for making predictions.
        data = {
            'TempHighF': TempHighF, 'TempAvgF': TempAvgF, 'TempLowF': TempLowF,
            'DewPointHighF': DewPointHighF, 'DewPointAvgF': DewPointAvgF, 'DewPointLowF': DewPointLowF,
            'HumidityHighPercent': HumidityHighPercent, 'HumidityAvgPercent': HumidityAvgPercent, 'HumidityLowPercent': HumidityLowPercent,
            'SeaLevelPressureHighInches': SeaLevelPressureHighInches, 'SeaLevelPressureAvgInches': SeaLevelPressureAvgInches, 'SeaLevelPressureLowInches': SeaLevelPressureLowInches,
            'VisibilityHighMiles': VisibilityHighMiles, 'VisibilityAvgMiles': VisibilityAvgMiles, 'VisibilityLowMiles': VisibilityLowMiles,
            'WindHighMPH': WindHighMPH, 'WindAvgMPH': WindAvgMPH, 'WindGustMPH': WindGustMPH, 'Events': selected_events,
            'Day': day, 'Year': year, 'Month': month
        }

       # The line `features_df = pd.DataFrame([data])` is creating a pandas DataFrame called
       # `features_df` from the `data` dictionary. The `data` dictionary contains the values of
       # various weather parameters and other features that are used for predicting rainfall.
        features_df = pd.DataFrame([data])

       # The line `predicted_rainfall = predict_rainfall(features_df)` is calling the
       # `predict_rainfall` function and passing the `features_df` DataFrame as an argument. This
       # function takes the input features, preprocesses them (such as encoding categorical variables
       # and standardizing numerical variables), and then uses a trained machine learning model to
       # make predictions on the standardized features. The predicted rainfall values are then stored
       # in the `predicted_rainfall` variable.
        predicted_rainfall = predict_rainfall(features_df)

       # The line `st.success(f"Predicted Rainfall: {predicted_rainfall[0]:.2f} inches")` is
       # displaying a success message in the Streamlit app interface.
        st.success(f"Predicted Rainfall: {predicted_rainfall[0]:.2f} inches")

# The `if __name__ == "__main__":` statement is a common Python idiom that checks whether the current
# script is being run as the main module or being imported as a module into another script.
if __name__ == "__main__":
    main()
