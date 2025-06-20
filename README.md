# 🎯 FitFusion – A Gym Website with Smart AI Chatbot

Welcome to *FitFusion* – a fully responsive, modern gym website designed to elevate the user experience by combining a stunning frontend interface with an intelligent AI-powered chatbot.

---

## 💻 Frontend – Designed for Fitness Lovers

The frontend of FitFusion is built using *HTML5, **CSS3, and **JavaScript*, offering a smooth, responsive, and visually appealing user experience. Visitors can:

- Explore gym membership plans
- Discover various workouts and classes
- Learn about trainers and schedules
- Navigate an intuitive, Gen-Z-friendly UI
- Interact with the website on both desktop and mobile devices

Everything is hand-coded with attention to detail, hover effects, and clean layout sections — perfect for a real gym business or a tech portfolio.

---

## 🤖 FitBot – Your AI-Powered Fitness Assistant

Integrated seamlessly into the site is *FitBot, an AI chatbot built with **Python, **Flask, and **Machine Learning*.

FitBot allows users to chat and ask about:

- 🏷️ Membership prices
- 🏋️ Workout plans
- 🕐 Gym timings
- 🧘‍♀️ Class types (Zumba, Yoga, HIIT, etc.)
- 🧑‍🏫 Trainer availability
- 🍎 Diet and nutrition plans
- 📍 Location & contact details
- 💡 Motivation and COVID safety

It uses NLP via *NLTK, vectorization via **scikit-learn*, and is trained on a custom intents.json file to understand real gym-related conversations.

The Flask backend handles message requests and dynamically returns responses, making the chatbot feel fast and interactive.

---

## 📦 Project Overview

The project is structured using Flask's MVC pattern:

- templates/ — contains index.html (main page)
- static/ — CSS & JS for chatbot frontend
- chatbot/ — Python files for training and predicting intents (train.py, predict.py)
- app.py — Flask app entry point
- intents.json — training data for chatbot
- classifier.pkl — saved ML model
- requirements.txt — all dependencies

---
## 📸 Screenshots



#### 🏠 Homepage  
![Image](https://github.com/user-attachments/assets/3da209bd-0774-4aa7-a022-bcbf26c40805)

#### 🤖 Chatbot Interaction  




## 🚀 Getting Started

bash
# Clone the repo
https://github.com/Arju-Mukhopadhyay/FitFusion

# Set up environment
python -m venv venv
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run the app
python app\app.py


Then open your browser at:

http://127.0.0.1:5000


---

## 🧠 Want to Train the Bot?

Modify intents.json and run:

bash
cd app/chatbot
python train.py


---

## ✨ Made By

- 💻 HTML, CSS, JavaScript (Frontend)
- 🧠 Python, Flask, Scikit-learn, NLTK (Backend & ML)
- 🧑‍💻 By Subhangi Banerjee, Progya Biswas, Arju Mukhopadhyay
