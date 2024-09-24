# Technical Assessment(Codematic) Project using Django(Backend) + React (Frontend)

## Overview

This project is a web application that combines Django for the backend and React for the frontend.
This application fetches details of a specific YouTube video such as Title, Description, View Count and Like Count using the YouTube Data API by inputting the YouTube Video ID.

## Features

- Displays YouTube Video Data
- Modern frontend built with React
- Robust backend built with Django

## Technologies Used

- Django
- Django REST Framework
- React
- Webpack
- Axios
- YouTube Video API (for video data functionality)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+
- Node.js and npm
- Django 3.2+
- A virtual environment tool (virtualenv, pipenv, etc.)(optional)

## Setup Instructions

### Backend (Django)

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install backend dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

### Frontend (React)

1. **Navigate to the frontend directory (react_frontend)**

    ```bash
    cd frontend
    ```

2. **Install frontend dependencies:**

    ```bash
    npm install
    ```

3. **Start the React development server:**

    ```bash
    npm run dev
    ```

## Usage

 **Access the application:**

    Open your browser and go to `http://localhost:3000/` for the React frontend OR `http://127.0.0.1:8000/api/video/?video_id=<input video id here>` for the Django backend.
   
    

## API Endpoints

Here are some of the key API endpoints provided by the Django backend:

- `GET /api/video/?video_id=<input video id here>` - Displays specified YouTube video details



## Contact

For any inquiries or issues, please contact [odararapheal@gmail.com].

