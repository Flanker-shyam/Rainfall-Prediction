import streamlit as st
import numpy as np
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler

# Placeholder function for predicting rainfall (replace with your model)
def predict_rainfall(features):
    
    # Convert the list of events to a string
    features['Events'] = features['Events'].apply(lambda x: ','.join(x) if isinstance(x, list) else x)

    encoder = LabelEncoder()
    features['Events'] = encoder.fit_transform(features['Events'])

    sc = StandardScaler()
    x_std = sc.fit_transform(features)
    x_std = pd.DataFrame(x_std, columns=features.columns)

    model = joblib.load('model_new.pkl')
    rainfall = model.predict(x_std)
    return rainfall

def main():

      # Customizing Streamlit page title and favicon
    st.set_page_config(
        page_title="Rainfall Prediction App",
        page_icon=":umbrella:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Adding styling with Markdown
    st.markdown(
        """
        <style>
            body {
                background-color: #f4f4f4;
            }
            .header {
                color: #1f4e79;
                font-size: 2em;
                padding: 20px;
                text-align: center;
                font-weight: bold;
            }
            .description {
                color: #333;
                font-size: 1.2em;
                padding: 20px;
                text-align: center;
            }
            .usage {
                color: #1f4e79;
                font-size: 1.5em;
                font-weight: bold;
                padding: 10px;
            }
            .button {
                background-color: #1f4e79;
                color: white;
                font-size: 1.2em;
                padding: 10px 20px;
                border-radius: 5px;
                margin-top: 20px;
                cursor: pointer;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Beautiful header
    st.markdown("<div class='header'>Rainfall Prediction App</div>", unsafe_allow_html=True)

    # Paragraph describing the app
    st.markdown("<div class='description'>This app predicts rainfall based on weather conditions.</div>", unsafe_allow_html=True)

    # st.title("Rainfall Prediction App")

    # Input variables
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

    # Multiselect dropdown for Events
    events_options = ["Rain", "Snow", "Thunderstorm", "Wind", "Fog"]
    selected_events = st.multiselect("Select Events", events_options)

    # Date selection
    day = st.slider("Day", min_value=1, max_value=31, value=15)
    month = st.slider("Month", min_value=1, max_value=12, value=6)
    year = st.slider("Year", min_value=2000, max_value=2023, value=2022)

    # Button to trigger prediction
    if st.button("Predict Rainfall"):
        # Create a feature dictionary from the selected values
        data = {
            'TempHighF': TempHighF, 'TempAvgF': TempAvgF, 'TempLowF': TempLowF,
            'DewPointHighF': DewPointHighF, 'DewPointAvgF': DewPointAvgF, 'DewPointLowF': DewPointLowF,
            'HumidityHighPercent': HumidityHighPercent, 'HumidityAvgPercent': HumidityAvgPercent, 'HumidityLowPercent': HumidityLowPercent,
            'SeaLevelPressureHighInches': SeaLevelPressureHighInches, 'SeaLevelPressureAvgInches': SeaLevelPressureAvgInches, 'SeaLevelPressureLowInches': SeaLevelPressureLowInches,
            'VisibilityHighMiles': VisibilityHighMiles, 'VisibilityAvgMiles': VisibilityAvgMiles, 'VisibilityLowMiles': VisibilityLowMiles,
            'WindHighMPH': WindHighMPH, 'WindAvgMPH': WindAvgMPH, 'WindGustMPH': WindGustMPH, 'Events': selected_events,
            'Day': day, 'Year': year, 'Month': month
              # Add selected events to the dictionary
        }

        # Create a DataFrame from the dictionary
        features_df = pd.DataFrame([data])

        # Get the predicted rainfall
        predicted_rainfall = predict_rainfall(features_df)
        # Display the result
        st.success(f"Predicted Rainfall: {predicted_rainfall[0]:.2f} inches")

if __name__ == "__main__":
    main()
