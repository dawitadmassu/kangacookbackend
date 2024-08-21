# KangaCook Order Backend

This repository contains the backend API for the KangaCook Order Application. The backend is built with Django and Django REST Framework and handles meal orders and customer management.

## Features

- **API for Orders**: Create, retrieve, update, and delete meal orders.
- **API for Customers**: Manage customer data and associate orders with customers.
- **Validation**: Enforces business rules like unique phone numbers for customers.

## Technologies

- **Django**: High-level Python web framework.
- **Django REST Framework**: Toolkit for building Web APIs with Django.

## Setup Instructions

1. **Clone the repository:**

```git clone https://github.com/yourusername/kangacook-order-backend.git```
2. **Navigate to the project directory:**

```cd kangacook-order-backend```
3. **Create and activate a virtual environment:**

```python -m venv venv```
```source venv/bin/activate```
4. **Install the dependencies:**
```pip install -r requirements.txt```
5. **Apply migrations:**
```python manage.py migrate```
6. **Start the development server:**
```python manage.py runserver```
