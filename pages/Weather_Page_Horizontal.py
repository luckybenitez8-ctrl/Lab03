
import streamlit as st
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="5-Day Weather Forecast", layout="wide")

st.title("5-Day Weather Forecast")

st.write("Enter a location (e.g., Atlanta, GA) to get the 5-day weather forecast with temperature and precipitation graphs.")

location = st.text_input("Location (City, State)", "Atlanta, GA")

def get_coordinates(location):
    try:
        response = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": location, "format": "json", "limit": 1},
            headers={"User-Agent": "streamlit-weather-app"}
        )
        data = response.json()
        if not data:
            return None
        return float(data[0]["lat"]), float(data[0]["lon"])
    except Exception as e:
        st.error(f"Geocoding failed: {e}")
        return None

def get_forecast(lat, lon):
    try:
        point_resp = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
        point_data = point_resp.json()
        forecast_url = point_data["properties"]["forecast"]

        forecast_resp = requests.get(forecast_url)
        forecast_data = forecast_resp.json()
        return forecast_data["properties"]["periods"]
    except Exception as e:
        st.error(f"Could not fetch weather data: {e}")
        return None

def extract_temperature_precip(forecast_periods):
    days = []
    temps = []
    pops = []
    for period in forecast_periods[:10]:
        days.append(period["name"])
        temps.append(period["temperature"])
        pops.append(period.get("probabilityOfPrecipitation", {}).get("value", 0))ax
    return days, temps, pops

if st.button("Get Forecast"):
    coords = get_coordinates(location)
    if coords:
        lat, lon = coords
        forecast_periods = get_forecast(lat, lon)
        if forecast_periods:
            st.success(f"Weather forecast for {location}")
            col1, col2 = st.columns([2, 3])
            with col1:
                for period in forecast_periods[:10]:
                    st.subheader(period["name"])
                    st.write(period["detailedForecast"])
            with col2:
                days, temps, pops = extract_temperature_precip(forecast_periods)
                st.subheader("Temperature Forecast")
                fig1, ax1 = plt.subplots()
                ax1.plot(days, temps, marker='o', linestyle='-', color='Blue')
                ax1.set_ylabel("Temperature (°F)")
                ax1.set_xticklabels(days, rotation=45, ha='right')
                st.pyplot(fig1)
                st.subheader("Precipitation Forecast")
                fig2, ax2 = plt.subplots()
                ax2.bar(days, pops, color='gray')
                ax2.set_ylabel("Precipitation Probability (%)")
                ax2.set_xticklabels(days, rotation=45, ha='right')
                st.pyplot(fig2)
        else:
            st.warning("No forecast data available.")
    else:
        st.warning("Invalid location input.")
