# Django Project

## 📌 About the Project
This project is a Django-based web application featuring news functionality and a main layout. It includes CRUD operations for managing news articles and a styled user interface.

---

## 🚀 Running the Project

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/talyx/django-newsblog
cd django-newsblog
```

### 2️⃣ Create and Activate a Virtual Environment
**Windows (cmd/Powershell):**
```sh
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux (bash/zsh):**
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt; cd newsblog
```

### 4️⃣ Make Migrations
```sh
python manage.py makemigrations
```

### 5️⃣ Apply Database Migrations
```sh
python manage.py migrate
```

### 6️⃣ Start the Django Server
```sh
python manage.py runserver
```

✅ Once started, the server will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🛠 Additional Commands

🔹 **Create a Superuser:**
```sh
python manage.py createsuperuser
```

🔹 **Update Dependencies:**
```sh
pip freeze > requirements.txt
```

🔹 **Deactivate Virtual Environment:**
```sh
deactivate
```

⚠️ Important!
This project is not optimized for different screen sizes or mobile devices. The interface is designed primarily for desktop browsers, and usability issues may occur on smartphones and tablets.

