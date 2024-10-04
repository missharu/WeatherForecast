# Weather Forecast - Climate Data Analysis 🌦️

This project collects real-time weather data from the OpenWeather API and saves it into a CSV file with information on temperature, humidity, and wind speed for a user-provided city. The interactive script allows the user to input the city's name, and the weather data is displayed in the terminal and saved for further analysis.

## Features

- Prompts the user to enter the name of a city.
- Retrieves real-time weather data from the OpenWeather API.
- Displays temperature, humidity, and wind speed information.
- Saves the data into a CSV file for future use.

## Project Structure

```bash
/WeatherForecast │
├── main.py # Main script that retrieves data and saves it to CSV
├── README.md # Project documentation
├── requirements.txt # Project dependencies (required libraries)
└── .gitignore # File to exclude unnecessary files from the repository
```


## Requirements

Make sure you have **Python 3.6+** installed. Additionally, you will need the following Python libraries:

- `requests`
- `pandas`

To install the dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## How It Works

This project uses the OpenWeather API to fetch real-time weather data. Through an HTTP request, the script retrieves information about the temperature, humidity, and wind speed of the user-provided city.

### Configuring the OpenWeather API
You will need an API key to access the OpenWeather data. Follow these steps:

- Visit the OpenWeather website and create an account.
- Generate an API key.
- Insert the API key in the Python script by replacing the value of the `api_key` variable in the `previsaotempo.py` file:

```bash
api_key = "YOUR_API_KEY"
```

## Usage

### Step 1: Clone the repository to your local machine

```bash
git clone https://github.com/your-username/previsaotempo.git
```

### Step 2: Navigate to the project directory

```bash
cd previsaotempo
```

### Step 3: Run the script

```bash
python previsaotempo.py
```

### Step 4: Enter the city name 

Enter the city name to retrieve weather data. The script will display the information in the terminal and save it into a CSV file with the city name.

## Author
This project was developed by Paula Carina Santos. If you have any questions or suggestions, feel free to reach out! 🌸

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
