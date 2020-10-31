# Machine Learning Service

## Aim
Aim of this project is the following
1. Learn how to use and set up Django
    - Also best practices for it
2. Host and contain (non-sensitive) machine learning projects that can be deployed onto a django backend

## How to use
First time setup:
```batch
virtualenv env
env\scripts\activate
pip install -r requirements.txt
```
**Alternatively, use pycharm and create a venv from there**

## Commands
Run django locally:
```batch
python manage.py runserver
```

Create new endpoint:
```batch
python manage.py startapp <app>
```

Database setup:
```batch
python manage.py migrate
```

Activate Models:
```batch
python manage.py makemigrations <app>
```



Open: `http://localhost:8000`


## Projects Available (Table of contents)
1. [Food Delivery Service (case study sample)](#food-delivery-service)

### Food delivery service 
Sample case study of a food delivery service and how it likely would be designed.
- Requirements and problem statement within `food_delivery folder`