# FitBuddy: AI Fitness Plan Generator using Gemini Models

FitBuddy is an AI-powered web application that generates **personalized 7-day workout plans, nutrition guidance, and recovery tips** based on a user's fitness goals. The application uses **Google Gemini** to create customized fitness plans and provides a real-time streaming experience for an interactive and engaging user experience.

## ✨ Features

* **⚡ Real-Time Streaming:** Watch your personalized 7-day workout plan generate live, character by character, for an instant and interactive experience.
* **🏋️ Personalized Workout Plans:** Generate customized 7-day workout plans based on fitness goals such as weight loss, muscle gain, fitness improvement, and general wellness.
* **🥗 Nutrition & Recovery Tips:** Receive AI-generated nutrition recommendations and recovery guidance tailored to your fitness goal.
* **🔄 Feedback Loop:** Submit feedback about your generated plan and receive an updated workout plan based on your feedback.
* **💾 SQLite Database:** Securely stores user information along with their original and updated fitness plans.
* **👨‍💼 Admin Dashboard:** Allows administrators to view registered users and their generated workout plans.
* **🤖 AI-Powered Generation:** Uses Google's Gemini model to generate personalized fitness recommendations.

## 🛠️ Tech Stack

### Backend

* **Python**
* **FastAPI**
* **SQLAlchemy**

### Database

* **SQLite**

### Frontend

* **HTML**
* **CSS**
* **JavaScript**
* **Jinja2 Templates**

### AI

* **Google Gemini**
* **`google-genai` SDK**
* **Gemini Interactions API**

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/tamilarasi281006/FitBuddy.git
cd FitBuddy
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API Key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your actual Google Gemini API key.

### 6. Run the Application

```bash
uvicorn app.main:app --reload
```

The application will be available locally at:

```text
http://127.0.0.1:8000
```

## 📂 Project Overview

FitBuddy follows a simple web application architecture:

```text
FitBuddy/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── templates/
│   └── static/
│
├── requirements.txt
├── .env
├── README.md
└── ...
```

## 🔄 Application Workflow

```text
User
  ↓
Enter Fitness Details & Goal
  ↓
FitBuddy Backend
  ↓
Google Gemini AI
  ↓
Generate 7-Day Fitness Plan
  ↓
Real-Time Streaming
  ↓
Workout + Nutrition + Recovery Tips
  ↓
User Feedback
  ↓
Updated Personalized Plan
  ↓
SQLite Database
```

## 🎯 Supported Fitness Goals

FitBuddy can generate plans based on goals such as:

* Weight Loss
* Muscle Gain
* General Fitness
* Strength Improvement
* Overall Wellness

## 🔐 Environment Variables

The application requires the following environment variable:

| Variable         | Description                                                       |
| ---------------- | ----------------------------------------------------------------- |
| `GEMINI_API_KEY` | Google Gemini API key used for AI-powered fitness plan generation |

> **Important:** Never commit your `.env` file or API key to GitHub. Add `.env` to your `.gitignore` file.

## 📌 Future Enhancements

* User authentication and authorization
* Progress tracking
* Workout completion tracking
* BMI and fitness-level analysis
* Weekly progress reports
* Personalized meal plans
* Workout history
* Advanced admin analytics
* Mobile-responsive improvements

## 📄 License

This project is developed for educational and academic purposes.
