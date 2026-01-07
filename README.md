🧾 Django Finance Tracker

A web-based Finance Tracking Application built using Django that allows users to manage income, expenses, and savings goals securely with authentication and authorization.

🚀 Features

User Registration & Login (Authentication)

Secure access using LoginRequiredMixin

Add, view, and manage Income & Expense transactions

Goal tracking with progress calculation

User-specific data isolation (each user sees only their data)
📁 Project Structure

django-finance-tracker/
│
├── Finance/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt

🔐 Authentication & Authorization

Implemented user authentication using Django’s built-in system

Used LoginRequiredMixin to restrict unauthorized access

Ensured data privacy by filtering records using request.user

Prevents users from accessing other users’ financial data

📊 Key Functionalities

Add Income & Expense transactions

Categorize transactions

Calculate total income, expenses, and savings

Set financial goals and track progress

Dashboard view with aggregated financial data

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/mayurik12/django-finance-tracker.git


Navigate to project directory

cd django-finance-tracker


Create virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Start the server

python manage.py runserver


Open browser:

http://127.0.0.1:8000/

🧪 Future Enhancements

Update & Delete transactions

Django REST API integration

Data visualization (charts)

Custom user model

Deployment on cloud platform

👩‍💻 Author

Mayuri Rajendra Kurhe
Python & Django Developer
GitHub: https://github.com/mayurik12

📌 Note

This project is developed for learning and academic purposes and demonstrates practical usage of Django authentication, authorization, and ORM concepts.
Dashboard with financial summary.



Clean and simple UI using Django Templates

🛠 Tech Stack

Backend: Python, Django

Frontend: HTML, CSS

Database: SQLite

Authentication: Django built-in auth system

Version Control: Git & GitHub
