import tkinter as tk
from tkinter import messagebox
from group_1_data_generator import TemperatureSensor

# Constants
LOW_TEMP = 18
NORMAL_TEMP = 22
HIGH_TEMP = 26
TEMP_UNIT = "°C"

# Initialize the sensor
sensor = TemperatureSensor()

# Window setup
window = tk.Tk()
window.title("Temperature Bar Display")
window.geometry('400x600')
window.configure(bg="#FFFFFF")

# Header
lblHeader = tk.Label(window, text="Temperature Data", font=("Arial Bold", 18), bg="#FFFFFF")
lblHeader.pack(pady=10)

# Sensor label setup
sensor_label = tk.Label(window, text=f"Sensor Data: {sensor.get_temperature():.2f}{TEMP_UNIT}", font=("Arial", 14), bg="#FFFFFF")
sensor_label.pack(pady=10)

# Canvas for temperature bar
canvas = tk.Canvas(window, width=150, height=220, bg="#F0F0F0", highlightthickness=1, highlightbackground="#CCCCCC")
canvas.pack(pady=10)

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
            draw_bar(new_value)
            sensor_label.config(text=f"Sensor Data: {new_value:.2f}{TEMP_UNIT}")
        else:
            messagebox.showerror("Error", f"Value must be between {LOW_TEMP} and {HIGH_TEMP}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

update_button = tk.Button(window, text="Update", command=update_value)
update_button.pack(pady=5)

def draw_bar(temp):
    canvas.delete("all")
    bar_height = int(((temp - LOW_TEMP) / (HIGH_TEMP - LOW_TEMP)) * 200)
    color = "green" if temp <= NORMAL_TEMP else "red"
    canvas.create_rectangle(50, 200 - bar_height, 100, 200, fill=color)
    # Tick labels
    canvas.create_text(110, 200, text=f"{LOW_TEMP}{TEMP_UNIT}", anchor="w", font=("Arial", 9))
    canvas.create_text(110, 0, text=f"{HIGH_TEMP}{TEMP_UNIT}", anchor="w", font=("Arial", 9))

# Real-time sensor update
def update_sensor():
    temp = sensor.generator_3()
    sensor_label.config(text=f"Sensor Data: {temp:.2f}{TEMP_UNIT}")
    draw_bar(temp)
    window.after(1000, update_sensor)

update_sensor()

def exit_program():
    window.destroy()

exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack(pady=5)

# Main loop
window.mainloop()