# Phase 7: Documentation

## How to Run the Project Locally

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

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory and add the required API key:

```env
GEMINI_API_KEY=your_api_key_here
```

> **Note:** Never upload your `.env` file or expose your API key in the GitHub repository.

### 6. Run the Application

Run the project using:

```bash
uvicorn app.main:app --reload
```

The application will start locally. Open the URL shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

### 7. Deactivate the Virtual Environment

After finishing:

```bash
deactivate
```

## Project Workflow

1. User enters their fitness details and goals.
2. FitBuddy processes the information using the configured Gemini AI model.
3. A personalized 7-day workout plan is generated.
4. Nutrition and recovery recommendations are provided.
5. Users can submit feedback.
6. The workout plan can be updated based on the feedback.
7. User-related data is stored using SQLite.

## Troubleshooting

### `requirements.txt` not found

Make sure you are inside the FitBuddy project directory:

```bash
cd FitBuddy
```

Then verify the file exists:

```powershell
dir
```

### Virtual environment is not activated

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

You should see `(venv)` at the beginning of the terminal prompt.

### API Key Error

Check that the `.env` file exists in the project root and that the Gemini API key is configured correctly.

## Technology Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python
* **AI Model:** Gemini
* **Database:** SQLite
* **Environment:** Python Virtual Environment
* **Version Control:** Git & GitHub
