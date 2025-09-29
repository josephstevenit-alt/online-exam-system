# 📝 Online Examination System

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-green)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB)](https://react.dev/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](#)

## 📖 Overview

The **Online Exam System** is a **full-stack web application** that allows users to **register, log in, and take exams online**.
It provides **secure authentication, dynamic question management, exam timer, automatic scoring, and result tracking**.
Designed with a **Flask backend** and **React.js frontend**, the system ensures **scalability, responsiveness, and modern UI/UX**.

---

## ✨ Features

* 🔑 **User Authentication** – Secure login & registration using JWT
* 👩‍💻 **Admin Panel** – Add, edit, and manage exams & questions
* 📝 **Take Exams** – Multiple-choice question support with exam timer
* 📊 **Auto Scoring & Results** – Real-time evaluation and result tracking
* 📱 **Responsive UI** – Mobile-friendly, clean, and modern design

---

## 🛠️ Technologies Used

**Backend:** Python, Flask, Flask-Migrate, SQLAlchemy, SQLite/MySQL
**Frontend:** React.js, Axios, React Router DOM, HTML5, CSS3
**Version Control & Hosting:** Git, GitHub

---

## 📂 Project Structure

```
online-exam-system/
│── backend/           # Flask backend
│   ├── app/
│   │   ├── routes/    # API routes (auth, exams, questions)
│   │   └── __init__.py
│   ├── migrations/    # Database migrations
│   ├── manage.py      # Flask app entry
│   ├── requirements.txt
│   └── run.py         # Run server script
│
│── frontend/          # React frontend
│   ├── public/
│   └── src/
│       ├── components/
│       ├── pages/
│       └── App.js
│
└── README.md
```

---

## ⚡ Setup Instructions

### 🔹 Backend Setup

```bash
git clone https://github.com/josephstevenit-alt/online-exam-system.git
cd online-exam-system/backend
```

Create & activate virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
set FLASK_APP=manage.py
set FLASK_ENV=development
flask db upgrade
```

Run backend server:

```bash
flask run
```

Backend runs on → **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

### 🔹 Frontend Setup

```bash
cd ../frontend
npm install
npm install axios react-router-dom
npm start
```

Frontend runs on → **[http://localhost:3000](http://localhost:3000)**

---

## 🚀 Deployment

* **Backend:** PythonAnywhere, Render, Railway, or Heroku
* **Frontend:** GitHub Pages, Netlify, or Vercel
* Update frontend API URLs to point to your deployed backend.

---

## 📸 Screenshots (Add later)

* Login Page
* Exam Interface with Timer
* Result Dashboard

---

## 🔗 Live Demo (Optional)

👉 [Demo Link Here](#) *(if deployed)*

---

## 📜 License

© 2025 **Joseph Anandhu**. All rights reserved.
This project is **proprietary** and cannot be copied or distributed without permission.

---

## 📬 Contact

👨‍💻 GitHub: [josephstevenit-alt](https://github.com/josephstevenit-alt)
📧 Email: [josephstevenit@gmail.com](mailto:josephstevenit@gmail.com)

