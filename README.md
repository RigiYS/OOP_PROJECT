# 🏐 Volleyball Training Tracker

This application is a final project for the Object-Oriented Programming (OOP) course. It is built using Python and applies full OOP principles. The app provides a simple GUI to log and review daily volleyball training sessions.

---

## 🎯 Application Inspiration

This application was inspired by my personal experience as a volleyball player and enthusiast. I often do various types of training such as **serving**, **passing**, **blocking**, and **spiking**, but I frequently forget to keep track of my progress. Therefore, I created the **Volleyball Training Tracker** app to record the duration and notes of each training session in an organized manner.

---

## 🔧 Features

- Add volleyball training sessions (Serve, Passing, Blocking, Spike)
- Record duration and notes for each session
- Automatically save training logs by date
- View today’s training log
- View all training logs from every date
- Simple GUI using Tkinter

---

## 📁 Folder Structure

volleyball_training_tracker/
├── main.py
├── 0705.mp4
├── models/
│ ├── init.py
│ ├── training_session.py
│ ├── serve_training.py
│ ├── passing_training.py
│ ├── blocking_training.py
│ ├── spike_training.py
│ └── training_log.py
├── data/
│ ├── init.py
│ └── data_manager.py
│ └── training_log.json
└── README.md

yaml
Copy
Edit

---

## 🚀 How to Run

### 1. Make sure Python is installed (Python 3.10 or higher)
### 2. Run the GUI application with the following command:

```bash
python main_gui.py
3. The GUI will appear:
Select the training type

Input duration (in minutes) and optional notes

Click Add Session

Use other buttons to view today's log or all logs

💻 Technologies Used
Python 3

OOP (Inheritance, Polymorphism, Abstract Class)

Tkinter (for GUI)

JSON (for local data storage)

🙋‍♂️ Contributor
Name: Muhammad Rigi Yuda Syahrial
Student ID: 20230040116
Class: TI23T
