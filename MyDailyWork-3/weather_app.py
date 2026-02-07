import tkinter as tk
from tkinter import messagebox
import requests

# -------- API KEY --------
API_KEY = "2707f4095ec290672ed10c715dd28959"

# -------- Function --------
def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("⚠️ Input Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        messagebox.showerror("❌ Error", data.get("message", "City not found"))
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    desc = data["weather"][0]["description"]

    result_label.config(
        text=f"""
📍 City: {city}
🌡 Temperature: {temp} °C
💧 Humidity: {humidity} %
🌬 Wind Speed: {wind} m/s
🌥 Condition: {desc.capitalize()}
"""
    )

# -------- GUI Window --------
root = tk.Tk()
root.title("🌦 Weather Forecast App")
root.geometry("420x420")
root.config(bg="#dff6ff")

# -------- Title --------
title_label = tk.Label(
    root,
    text="🌈 Weather Forecast 🌈",
    font=("Arial", 20, "bold"),
    bg="#dff6ff"
)
title_label.pack(pady=15)

# -------- City Input --------
city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=25
)
city_entry.pack(pady=10)

# -------- Button --------
get_button = tk.Button(
    root,
    text="🔍 Get Weather",
    font=("Arial", 13, "bold"),
    bg="#4da8da",
    fg="white",
    padx=10,
    pady=5,
    command=get_weather
)
get_button.pack(pady=15)

# -------- Result --------
result_label = tk.Label(
    root,
    text="☁️ Weather details will appear here",
    font=("Arial", 13),
    bg="#dff6ff",
    justify="left"
)
result_label.pack(pady=20)

# -------- Footer --------
footer_label = tk.Label(
    root,
    text="✨ Stay updated. Stay safe. ✨",
    font=("Arial", 10, "italic"),
    bg="#dff6ff"
)
footer_label.pack(side="bottom", pady=10)

# -------- Run --------
root.mainloop()