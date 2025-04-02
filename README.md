# Temperature Sensor GUI Displays

This project is part of the Networking for Software Developers course. It demonstrates interactive display interfaces for simulated temperature data, based on Lab 6.

---

## 📦 Contents

- `group_1_data_generator.py`  
  Generates realistic temperature data using random noise, Gaussian curves, and incremental change simulation.

- `group_1_display_bar.py`  
  A Tkinter GUI that displays the temperature as a vertical bar chart with real-time updates and manual input.

- `group_1_display_gauge.py`  
  A Tkinter GUI that displays the temperature on a circular gauge with a rotating needle.

- `lab9_display_chart/group_1_display_chart.py`  
  ➤ Displays a static chart of temperature data using both **bar** and **line** overlays. User can control data range displayed.

---

## ✅ Features

- Real-time sensor simulation (bar & gauge)
- Static chart slice display (Lab 9)
- Manual value entry with validation
- Unit labels, normal range hints, out-of-range detection
- Aesthetic layout and responsive GUI designs
- Smooth integration with course lab requirements

---

## 📊 Lab 9 – Display Chart

**File:** `lab9_display_chart/group_1_display_chart.py`

This GUI visualizes 20 pre-generated temperature values with:
- **6 bars and a red line graph** showing selected slices
- **Responsive resizing**
- **User-friendly interface**: validation, hints, dynamic chart redrawing
- Temperature values shown above bars

### 🔧 How to Use

1. Open the terminal:
```bash
cd lab9_display_chart
python group_1_display_chart.py

