# Temperature Sensor GUI Displays

This project is part of the *Networking for Software Developers* course. It demonstrates interactive display interfaces for simulated temperature data, based on Lab 6.

## 📦 Contents

- `group_1_data_generator.py`  
  Generates realistic temperature data using random noise, Gaussian curves, and incremental change simulation.

- `group_1_display_bar.py`  
  A Tkinter GUI that displays the temperature as a vertical bar chart with real-time updates and manual input.

- `group_1_display_gauge.py`  
  A Tkinter GUI that displays the temperature on a circular gauge with a rotating needle.

## ✅ Features

- Real-time sensor simulation
- Manual value entry with validation
- Description of units, normal range, and extremes
- Visual indicators for bar height and gauge angle
- Aesthetic layout and responsive design

## 💻 Requirements

- Python 3.7+
- `matplotlib` (used in data generator for standalone plotting)

Install with:
```bash
pip install matplotlib
