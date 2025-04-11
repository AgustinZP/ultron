# 🧠 Ultron API - Technical Challenge (J.A.R.V.I.S.)

This is a Python project built with **FastAPI** following a **DDD (Domain-Driven-Design)** structure and a hexagonal architecture.
It solves a 3-part technical challenge.

## 🚀 Technologies Used
- **FastAPI**
- **Python 3.13.1**
- **Uvicorn**
- **Requests**
- **dotenv**
- **pipenv**
- **pytest**

## ⚙️ Setup Instructions

### 1. Clone repository

### 2. Install dependencies

to install with `pipenv install`

### 3. In file .env.example should change url and candidate_key for the right ones

`BASE_URL=https://jarvis.dev/api`

`CANDIDATE_KEY=your_api_key_here`

### 4. Run the FastAPI server

tu run FastAPI server with `pipenv run uvicorn main:app --reload`

To test an endpoint, visit:

- `http://127.0.0.1:8000/problem1`
- `http://127.0.0.1:8000/problem2`
- `http://127.0.0.1:8000/problem3`

or run `pipenv run python command.py` to solve problems in console

Docs available at `http://localhost:8000/docs`

## 🧪 Tests

to run tests `pipenv run pytest`