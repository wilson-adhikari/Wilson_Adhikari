import customtkinter as ctk
import requests
import tkinter as tk


def get_weather(city_name):
    city_name = entry.get().strip().lower()
    if city_name is None:
        print(f'not found {city_name}')
        return None
    else:
        api_key = "b3c8137cb668470f69e4b9eb283dba42"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        return data

def display_weather(data):
    progress_bar.stop()
    progress_bar.pack_forget()
    unit = "°C" if unit_var.get() == "metric" else "°F"
    weather_text = (
        f"weather in {unit}\n"
        f"City: {data['name']}\n"
        f"Temperature: {data['main']['temp'] - 273.15:.2f}°C\n"
        f"Description: {data['weather'][0]['description']}\n"
        f"Pressure: {data['main']['pressure']} hPa\n"
        f"Humidity: {data['main']['humidity']}%\n"
        f"Wind Speed: {data['wind']['speed']} m/s\n"
        f"Cloudiness: {data['clouds']['all']}%"
    )
    if data is None:
        weather_text = "City not found"
    else:
        print(f"Weather in {unit}")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp'] - 273.15:.2f}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Pressure: {data['main']['pressure']} hPa")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Cloudiness: {data['clouds']['all']}%")
        print(f"\n")

    weather_label.configure(text=weather_text)
def fetch_weather():
    progress_bar.pack(anchor="center", pady=5)
    progress_bar.start()
    root.after(100, lambda: display_weather(get_weather(entry.get())))
    




root = ctk.CTk()
root.geometry("600x400")
root.title("weather app")
root.resizable(False, False)

label = tk.Label(root, text="Enter city name:",font= ctk.CTkFont(size=20, weight="bold",underline=True))
label.pack(pady=20)

entry = tk.Entry(root,background="white",width=30,font=("Arial", 12))
entry.pack(pady=10)
entry.bind("<Return>", lambda event: fetch_weather())

unit_var = tk.StringVar(value="metric")
unit_frame = ctk.CTkFrame(root)
unit_frame.pack(pady=5)

C=ctk.CTkRadioButton(unit_frame, text="°C", variable=unit_var, value="metric").pack(side="left", padx=10)
F=ctk.CTkRadioButton(unit_frame, text="°F", variable=unit_var, value="imperial").pack(side="left", padx=10, anchor="center")

button = ctk.CTkButton(root, text="Get Weather", command= fetch_weather,font=("Arial", 13),anchor="center")
button.pack(anchor="center")

progress_bar = ctk.CTkProgressBar(root, mode="indeterminate", orientation="horizontal", width=200)


weather_label = ctk.CTkLabel(root, text="",font=("Arial", 15))
weather_label.pack(anchor="center",pady=10)

root.mainloop()
