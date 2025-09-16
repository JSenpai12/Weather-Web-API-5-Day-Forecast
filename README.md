
# Weather App

A real-time weather dashboard built with **Flask** and **OpenWeather API**. This app automatically detects the user's location using their IP address and displays:

- Current weather conditions
- 5-day weather forecast
- Temperature, feels like, humidity, wind speed, visibility
- Weather icons that change based on conditions
- Last updated time and date

---

## **Features**

- Automatic location detection via IP
- Current weather display
- 5-day forecast display
- Dynamic weather icons for each day
- Responsive design using HTML, CSS, and JavaScript
- Easy to extend for additional features like UV index, sunrise/sunset, etc.

---

## **Installation**

1. Clone the repository:
```bash
git clone https://github.com/your-username/weather-app.git

2. Navigate into the directory:

```bash
cd weather-app
```

3. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Add your **OpenWeather API key** in `app.py`:

```python
api_key = "YOUR_API_KEY"
```

6. Run the Flask app:

```bash
python app.py
```

7. Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## **Usage**

* Click the **refresh button** to update weather data.
* View the **current weather** at the top.
* Scroll down to see the **5-day forecast** with high/low temperatures and weather icons.

---

## **Folder Structure**

```
weather-app/
│
├── templates/
│   └── index.html       # HTML frontend
├── static/
│   ├── css/             # CSS files
│   └── js/              # JavaScript files
├── app.py               # Flask backend
└── README.md
```

---

## **Technologies Used**

* Python 3.x
* Flask
* OpenWeather API
* HTML, CSS, JavaScript
* Fetch API for AJAX calls

---

## **License**

This project is open source and available under the [MIT License](LICENSE).

---

## **Screenshots**

<img width="1867" height="881" alt="Screenshot 2025-09-16 150628" src="https://github.com/user-attachments/assets/2e0804e6-5549-450c-a3dc-a503ed93cfe3" />


---

## **Contributing**

Feel free to fork this repository, create issues, and submit pull requests. Suggestions for features or improvements are welcome!

---

```

---

