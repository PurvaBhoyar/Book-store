# Django Bookstore Management System


![Screenshot 2025-04-25 191233](https://github.com/user-attachments/assets/41502051-e54f-4a3d-914f-2b58279fdaf7)
![Screenshot 2025-04-25 191241](https://github.com/user-attachments/assets/07ea46f8-cff1-4745-a86a-06070967666e)
![Screenshot 2025-04-25 191253](https://github.com/user-attachments/assets/a27e4575-c7de-4a7f-a178-5db41802bf43)

![Screenshot 2025-04-25 191604](https://github.com/user-attachments/assets/f9313b5f-31ea-441a-97d6-1e6281ee9d00)
![Screenshot 2025-04-25 191527](https://github.com/user-attachments/assets/b884b583-5bdc-4cc4-8b7f-27a379e9906f)
![Screenshot 2025-04-25 191542](https://github.com/user-attachments/assets/5d660009-dc37-453a-8040-2be8adb02ed6)
![Screenshot 2025-04-25 191553](https://github.com/user-attachments/assets/a9dda03e-ad65-4b9b-86ca-88b6668f0adb)

![Screenshot 2025-04-25 191727](https://github.com/user-attachments/assets/d5805679-a5b4-41b0-91c3-46f3ca04ddd0)
![Screenshot 2025-04-25 191744](https://github.com/user-attachments/assets/eddefdac-b034-4946-98ac-4f29f558c027)

![Screenshot 2025-04-25 191611](https://github.com/user-attachments/assets/405264c5-e506-41a9-940a-ff86b080ffea)
![Screenshot 2025-04-25 191616](https://github.com/user-attachments/assets/410b030b-0215-4e0f-8f48-d7c27476db21)


A complete bookstore management system built with Django, featuring user authentication, admin panel, and shopping cart functionality. Dockerized for easy deployment with CI/CD pipeline support.

## Features

- User authentication (register/login/logout)
-  Custom admin panel (add/edit/delete books)
-  Session-based shopping cart
-  Responsive design with Bootstrap
-  Docker containerization
-  CI/CD pipeline with Jenkins

## Tech Stack

**Backend:**
- Python 
- Django 

**Frontend:**
- HTML5, CSS3
- Bootstrap 5
- JavaScript

**DevOps:**
- Docker
- Docker Compose
- Jenkins
- GitHub Actions

## Setup & Installation

### 1. Clone the repository
Without Docker
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```
```bash
git clone https://github.com/your-username/django-bookstore.git
cd django-bookstore
cp .env.example .env
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
