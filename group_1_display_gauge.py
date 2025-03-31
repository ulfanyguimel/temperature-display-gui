import tkinter as tk
from tkinter import messagebox
from math import cos, sin, radians
from group_1_data_generator import TemperatureSensor

# Constants
LOW_TEMP = 18
NORMAL_TEMP = 22
HIGH_TEMP = 26
TEMP_UNIT = "°C"

# Initialize the sensor
sensor = TemperatureSensor()

# Main application window
window = tk.Tk()
window.title("Temperature Gauge Display")
window.geometry("500x600")
window.configure(bg="#FFFFFF")

# Header
lblHeader = tk.Label(window, text="Temperature Gauge", font=("Arial Bold", 18), bg="#FFFFFF")
lblHeader.pack(pady=10)

# Sensor label setup
sensor_label = tk.Label(window, text=f"Sensor Data: {sensor.get_temperature():.2f}{TEMP_UNIT}", font=("Arial", 14), bg="#FFFFFF")
sensor_label.pack(pady=10)

# Canvas for gauge
gauge_canvas = tk.Canvas(window, width=300, height=200, bg="#FFFFFF", highlightthickness=0)
gauge_canvas.pack(pady=10)

# Additional information
info_label = tk.Label(window, text=f"Units: {TEMP_UNIT}\nLow: {LOW_TEMP}{TEMP_UNIT}\nNormal: {NORMAL_TEMP}{TEMP_UNIT}\nHigh: {HIGH_TEMP}{TEMP_UNIT}", font=("Arial", 12), bg="#FFFFFF")
info_label.pack(pady=10)

# Entry and Button to update the value
value_entry = tk.Entry(window, font=("Arial", 12))
value_entry.pack(pady=5)

def update_value():
    try:
        new_value = float(value_entry.get())
        if LOW_TEMP <= new_value <= HIGH_TEMP:
            draw_gauge(new_value)
            sensor_label.config(text=f"Sensor Data: {new_value:.2f}{TEMP_UNIT}")
        else:
            messagebox.showerror("Error", f"Value must be between {LOW_TEMP} and {HIGH_TEMP}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

update_button = tk.Button(window, text="Update", command=update_value)
update_button.pack(pady=5)

def draw_gauge(temp):
    gauge_canvas.delete("all")
    # Draw base arc
    gauge_canvas.create_arc(20, 20, 280, 280, start=0, extent=180, style='arc', width=3)

    # Draw tick marks and labels
    for t in range(LOW_TEMP, HIGH_TEMP + 1, 2):
        angle = 180 - ((t - LOW_TEMP) / (HIGH_TEMP - LOW_TEMP) * 180)
        x0 = 150 + 120 * cos(radians(angle))
        y0 = 150 - 120 * sin(radians(angle))
        x1 = 150 + 100 * cos(radians(angle))
        y1 = 150 - 100 * sin(radians(angle))
        gauge_canvas.create_line(x0, y0, x1, y1, width=2)
        label_x = 150 + 80 * cos(radians(angle))
        label_y = 150 - 80 * sin(radians(angle))
        gauge_canvas.create_text(label_x, label_y, text=str(t), font=("Arial", 8))

    # Draw needle
    angle = 180 - ((temp - LOW_TEMP) / (HIGH_TEMP - LOW_TEMP) * 180)
    needle_x = 150 + 90 * cos(radians(angle))
    needle_y = 150 - 90 * sin(radians(angle))
    gauge_canvas.create_line(150, 150, needle_x, needle_y, width=3, fill="red")
    gauge_canvas.create_oval(145, 145, 155, 155, fill="black")

def update_sensor():
    temp = sensor.generator_3()
    draw_gauge(temp)
    sensor_label.config(text=f"Sensor Data: {temp:.2f}{TEMP_UNIT}")
    window.after(1000, update_sensor)

update_sensor()

def exit_program():
    window.destroy()

exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack(pady=5)

window.mainloop()
