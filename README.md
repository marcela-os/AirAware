
## 🌬 AirAware

App for monitoring air quality in Poland.
Application using data from the General Inspectorate for Environmental Protection (GIOŚ).

---

## 🛠️ Functions


- Fetches real-time air quality measurement data from GIOŚ REST API.
- Allows searching for monitoring stations by location name or proximity (within a radius in km).
- Displays air quality index and sensor data on maps.
- Displays air quality index data and parameters from selected stations.
- Interactive GUI with multiple pages.
- Presents data in interactive charts.
- Provides simple data analysis: minimum, maximum, average, and trends.
- Uses Singleton pattern to manage and reload data.
- Handles connection errors gracefully and informs the user accordingly.
- Modular codebase with clear logical separation (e.g., data fetching, storage, GUI, analysis).
- Equipped with comprehensive docstrings and unit tests.


---

## 🚀 Tech Stack

 - Python 3.12.10
 - SQLite for local data storage
 - Requests for REST API calls
 - Pandas for data manipulation
 - Geopy for geolocation and distance calculations
 - Plotly for charts 
 - GUI framework Taipy

---
##  🧑‍💻 Usage

Select a monitoring station from the full list or filter by city name.

Search stations near a specific location by entering a description (e.g., “Poznań dworzec”) and a radius in km.

View current and historical measurements for selected sensors.

Visualize data with charts and maps.

Perform simple statistical analyses on measurement data (min, max, average, trends).

If live data is unavailable due to connection issues, the app can use stored data in database.

---
## 🏃🏻‍♀️ Installation & run

Instalation
* Clone the repository

```bash
  git clone https://github.com/marcela-os/AirAware.git
  
  cd airaware
```

* Install the required dependencies

```bash
  pip install -r requirements.txt
```

* Start the application

```bash
  python main.py
```
---

## ˙✧˖° Author ˙✧˖°

 [@marcelaos](https://github.com/marcela-os)
