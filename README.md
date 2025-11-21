# FastAPI Application

1. Install Dependencies

Make sure you have **Python 3.9+** installed.

2. Activate the virtual environment

python -m venv venv


venv\Scripts\activate

3. Install the dependencies

pip install -r requirements.txt

4. Start the Server

Run the FastAPI application with uvicorn:

uvicorn app.main:app --reload

Your server will run at:

http://127.0.0.1:8000/docs
