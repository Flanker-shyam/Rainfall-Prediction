
<h1>Rainfall Prediction Web App</h1>

<h2>Overview</h2>
<p>This Rainfall Prediction Web App allows users to predict rainfall for a specific date using a machine learning model. Users can either manually enter weather data or input only the date, and the backend fetches additional information from the OpenWeatherMap API to make predictions.</p>

<h2>Requirements:</h2>
To set up the virtual environment and install the required libraries, run the following commands:

<b>1. Clone the repository to your local machine:<b>
```bash
git clone https://github.com/Flanker-shyam/Rainfall-Prediction.git
```
<b>2. Navigate into the project directory:<b>
```bash
cd Rainfall-Prediction
```
<b>3. Create a new Python virtual environment (recommended):<b>
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
.\venv\Scripts\activate  # On Windows
```
<b>4. Install the dependencies using pip:<b>
```bash
pip install -r requirements.txt
```

<h2>How to Use:</h2>
To launch the web app, simply run the following command:

```bash
streamlit run Rainfall_main.py
```

Once the web app is launched, you can either enter the entire dataset manually or just the date for which you want to get the rainfall prediction.

<h2>Features</h2>
<ul>
<li>Manual Input: Users can enter weather data manually.</li>
<li>Date-Based Prediction: Users can input a specific date, and the app fetches additional weather information from OpenWeatherMap to make predictions.</li>
<li>Machine Learning Model: The app uses a machine learning model for rainfall predictions.</li>
<li>Responsive UI: The Streamlit app provides an intuitive and user-friendly interface.</li>
</ul>

<h2>Acknowledgements:</h2>
<p></p>We would like to express our gratitude to the Streamlit team for creating this user-friendly Python library.
We would also like to thank the [OpenWeatherMap team]([url](https://openweathermap.org/) for providing the Weather API used in this project.</p>
