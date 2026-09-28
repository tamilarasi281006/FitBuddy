# Phase 5: Development
- Built a **FastAPI** backend with routes: `/`, `/generate-workout`, `/stream-workout`, `/generate-tip`, `/submit-feedback`, `/view-all-users`.
- Integrated the **Google Gemini API** using the `google-genai` SDK — Gemini Pro for workout plans and Gemini Flash for nutrition tips.
- Implemented **live streaming** of workout plans using `StreamingResponse`.
- Built a responsive frontend with **Jinja2 templates** and custom **CSS**.
- Persisted users and plans in **SQLite** via `database.py`.
- Secured API keys using a `.env` file and `python-dotenv`.