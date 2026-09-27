## ✨ Features
- **Real-Time Streaming:** Watch your 7-day workout plan generate live, character by character, for an instant, interactive experience.
- **Personalized Workouts:** Generated using the Gemini 3.8 Flash model.
- **Nutrition & Recovery Tips:** Tailored tips based on your goal.
- **Feedback Loop:** Users can submit feedback and get an updated plan instantly.
- **SQLite Database:** Stores users and their original + updated plans.
- **Admin Dashboard:** View all users and their plans.# FitBuddy: AI Fitness Plan Generator using Gemini Models

FitBuddy is a web-based application that uses AI to generate personalized 3-day workout plans and nutrition tips based on a user's fitness goals, such as weight loss, muscle gain, or general wellness. The app streams the workout plan in real-time for an instant, interactive experience.

## ✨ Features
- **Real-Time Streaming:** Watch your 3-day workout plan generate live, character by character.
- **Personalized Workouts:** Generated using the Gemini 3.8 Flash model.
- **Nutrition & Recovery Tips:** Tailored tips based on your goal.
- **Feedback Loop:** Users can submit feedback and get an updated plan instantly.
- **SQLite Database:** Stores users and their original + updated plans.
- **Admin Dashboard:** View all users and their plans.

## 🛠️ Tech Stack
- **Backend:** FastAPI, Python, SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript, Jinja2
- **AI:** Google Gemini (`gemini-3.8-flash`) via the `google-genai` SDK (Interactions API)

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/tamilarasi281006/FitBuddy.git
   cd FitBuddy

   # FitBuddy

An AI-powered fitness and nutrition assistant built with FastAPI and Google Gemini.

## Features
- Generate personalized workout plans
- Get nutrition tips
- Update plans based on user feedback
- View all users and their plans

## Setup
1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your `GEMINI_API_KEY`
6. Run: `uvicorn app.main:app --reload`