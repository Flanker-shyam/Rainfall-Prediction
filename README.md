
<h1>Rainfall Prediction Web App</h1>

<h2>Overview</h2>
<p>This Rainfall Prediction Web App allows users to predict rainfall for a specific date using a machine learning model. Users can either manually enter weather data or input only the date, and the backend fetches additional information from the OpenWeatherMap API to make predictions.<p>

<h2>Requirements:</h2>
To set up the virtual environment and install the required libraries, run the following commands:

<b>1. Clone the repository to your local machine:<b>
```bash
git clone https://github.com/your_username/your_project.git
```
<b>2. Navigate into the project directory:<b>
```bash
cd your_project
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

<h2>Features<h2>
<ol>
<l1>Manual Input: Users can enter weather data manually.</l1>
<l1>Date-Based Prediction: Users can input a specific date, and the app fetches additional weather information from OpenWeatherMap to make predictions.</l1>
<l1>Machine Learning Model: The app uses a machine learning model for rainfall predictions.</l1>
<l1>Responsive UI: The Streamlit app provides an intuitive and user-friendly interface.</l1>
</ol>

<h2>License</h2>
This project is licensed under the MIT License.

<h2>Acknowledgements:</h2>
We would like to express our gratitude to the Streamlit team for creating this user-friendly Python library.

We would also like to thank the OpenWeatherMap team for providing the Weather API used in this project.