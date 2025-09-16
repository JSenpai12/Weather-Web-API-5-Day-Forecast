weatherData();
fiveDayForecast();
const refreshBtn = document.querySelector('.refresh-btn');

if (refreshBtn) {
  refreshBtn.addEventListener('click', (e) => {
    e.target.style.transform = 'rotate(360deg)';
    e.target.style.transition = 'transform 0.6s ease';

    setTimeout(() => {
      e.target.style.transform = 'none';
      e.target.style.transition = 'none';
    }, 600);

    console.log('Hi');

    weatherData();
  });
}

async function weatherData() {
    try {
        let response = await fetch("/current", {method: "POST"});
        let data = await response.json()

        document.querySelector('.city-title').innerText = data.city;
        document.querySelector('.temperature').innerText = `${data.temperature}°`;
        document.querySelector('.condition-title').innerText = data.weather;
        document.querySelector('.condition-desc').innerText = data.description;
        document.querySelector('.feels-like').innerText = data.feels_like;
        document.getElementById('humid').innerText = `${data.humidity}%`;
        document.getElementById('windspeed').innerText = `${data.windspeed} km/h`;
        document.getElementById('visibility').innerText = `${data.visibility / 1000} km`;
        document.getElementById('maxtemp').innerText = data.temp_max;
        document.querySelector('.update-date').innerText = data.lastUpdateDate;
        document.querySelector('.update-time').innerText = data.lastUpdateTime;

    } catch(error) {
        console.error(error)
    }
    
}

async function fiveDayForecast() {
  try {
    let response = await fetch("/forecast", {method: "POST"});
    let data = await response.json();

    console.log(data.forecast);
     

    //# Current Day
    document.getElementById('forecastCondition1').innerText = data.forecast[0].description;
    document.getElementById('forecastHigh1').innerText = `${data.forecast[0].temp}°`;
    document.getElementById('forecastLow1').innerText = `${data.forecast[0].feels_like}°`;
    document.getElementById(`forecastIcon1`).src = `https://openweathermap.org/img/wn/${data.forecast[0].icon}@2x.png`;
    document.getElementById(`forecastIcon0`).src = `https://openweathermap.org/img/wn/${data.forecast[0].icon}@2x.png`;

    for (let i = 2; i <= 5; i++) {
      document.getElementById(`forecastDay${i}`).innerText = data.forecast[i-1].day;
      document.getElementById(`forecastCondition${i}`).innerText = data.forecast[i-1].description;
      document.getElementById(`forecastHigh${i}`).innerText = `${data.forecast[i-1].temp}°`;
      document.getElementById(`forecastLow${i}`).innerText = `${data.forecast[i-1].feels_like}°`;
      document.getElementById(`forecastIcon${i}`).src = `https://openweathermap.org/img/wn/${data.forecast[i-1].icon}@2x.png`;
    }


  } catch(error) {
    console.error(error)
  }
  
}

