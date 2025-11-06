
import streamlit as st
import requests

st.set_page_config(page_title="5-Day Weather Forecast", layout="centered")

st.title(" 5-Day Weather Forecast")

st.write("Enter a location (e.g., Atlanta, GA) to get the 5-day weather forecast.")

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

if st.button("Get Forecast"):
    coords = get_coordinates(location)
    if coords:
        lat, lon = coords
        forecast_periods = get_forecast(lat, lon)
        if forecast_periods:
            st.success(f"Weather forecast for {location}")
            for period in forecast_periods[:10]:
                st.subheader(period["name"])
                st.write(period["detailedForecast"])
        else:
            st.warning("No forecast data available.")
    else:
        st.warning("Invalid location input.")
