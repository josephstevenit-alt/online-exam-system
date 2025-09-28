# Online Exam System

![Online Exam System](https://img.shields.io/badge/Status-Completed-brightgreen)

## Overview
The **Online Exam System** is a full-stack web application that allows users to register, login, and take exams online. The system is built with **Flask** for the backend and **React.js** for the frontend. It supports secure user authentication, dynamic question management, and exam result tracking.

---

## Features
- User registration and login with authentication
- Admin panel to add/edit exams and questions
- Take exams with multiple-choice questions
- Automatic scoring and result tracking
- Fully responsive and modern UI

---

## Technologies Used
**Backend:** Python, Flask, Flask-Migrate, SQLAlchemy, SQLite/MySQL  
**Frontend:** React.js, Axios, React Router DOM, HTML5, CSS3  
**Version Control & Hosting:** Git, GitHub  

---

## Project Structure
online-exam-system/
│
├── backend/ # Flask backend
│ ├── app/
│ │ ├── routes/ # API routes for auth, exams, questions
│ │ └── init.py
│ ├── migrations/ # Database migrations
│ ├── manage.py # Flask app entry
│ ├── requirements.txt # Python dependencies
│ └── run.py # Run server script
│
├── frontend/ # React frontend
│ ├── public/
│ └── src/
│ ├── components/
│ ├── pages/
│ └── App.js
│
└── README.md

yaml
Copy code

---

## Setup Instructions

### Backend
1. Clone the repository:
```bash
git clone https://github.com/josephstevenit-alt/online-exam-system.git
cd online-exam-system/backend
Create a virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
set FLASK_APP=manage.py
set FLASK_ENV=development
flask db upgrade
Run the backend server:

bash
Copy code
flask run
Frontend
Navigate to frontend:

bash
Copy code
cd ../frontend
Install dependencies:

bash
Copy code
npm install
npm install axios react-router-dom
Start the frontend:

bash
Copy code
npm start
Frontend runs on http://localhost:3000

Backend API runs on http://127.0.0.1:5000

Deployment
Backend: Host on PythonAnywhere, Render, or Railway

Frontend: Host on GitHub Pages, Netlify, or Vercel

Update frontend API URLs to point to your deployed backend URL.

License & Copyright
pgsql
Copy code
© 2025 Joseph Anandhu. All rights reserved.
This project is proprietary and cannot be copied or distributed without permission.
Contact
GitHub: https://github.com/josephstevenit-alt

Email: your.email@example.com

yaml
Copy code

---

If you want, I can also **add badges, screenshots, and a live demo link section** to make this README **look professional and eye-catching on GitHub**.  

Do you want me to do that next?
