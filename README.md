# Hospital Management System API

A Hospital Management System REST API built with **Django REST Framework** and **PostgreSQL**. This project provides backend functionality for managing hospital operations, including users, departments, doctors, patients, appointments, and prescriptions.

## Features

- User Registration and Authentication
- JWT Authentication
- Role-Based User Management
- Department Management
- Doctor Management
- Patient Management
- Appointment Management
- Prescription Management
- RESTful API Endpoints
- Database Integration with PostgreSQL
- CRUD Operations (Create, Read, Update, Delete)

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- Thunder Client

## Project Structure

```text
Hospital-Management-System-API/
│
├── accounts/
├── core/
├── departments/
├── doctors/
├── patients/
├── appointments/
├── prescriptions/
│
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/HajiraYousuf/Hospital-Management-System-API.git
```

### 2. Navigate to the Project

```bash
cd Hospital-Management-System-API
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file and configure your database settings:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=hospital_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### 7. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create Superuser

```bash
python manage.py createsuperuser
```

### 9. Start Development Server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

| Module | Endpoint |
|---|---|
| Register | `/api/auth/register/` |
| Login | `/api/auth/login/` |
| Users | `/api/auth/users/` |
| Departments | `/api/departments/` |
| Doctors | `/api/doctors/` |
| Patients | `/api/patients/` |
| Appointments | `/api/appointments/` |
| Prescriptions | `/api/prescriptions/` |

## API Testing

All API endpoints can be tested using **Thunder Client** or **Postman**.

Supported HTTP methods:

- `GET` – Retrieve data
- `POST` – Create new records
- `PUT` – Update existing records
- `PATCH` – Partially update records
- `DELETE` – Remove records

## Authentication

This project uses JWT (JSON Web Token) authentication to secure protected API endpoints.

Include the access token in the Authorization header:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## User Roles

- **Admin:** Manages hospital data and staff.
- **Doctor:** Manages doctor-related information.
- **Patient:** Represents registered hospital patients.
- **Receptionist:** Supports appointment and patient management.

## Project Purpose

This project was developed as part of the **DecodeLabs Full Stack Development Industrial Training Program – Project 3**.

It demonstrates practical knowledge of backend development, database integration, REST API design, authentication, and CRUD operations.

## Author

**Hajira Yousuf Ali**

- GitHub: [@HajiraYousuf](https://github.com/HajiraYousuf)
- LinkedIn: [Hajira Yousuf](https://linkedin.com/in/hajira-yousuf/)

---

*Built with Django REST Framework and PostgreSQL.*
