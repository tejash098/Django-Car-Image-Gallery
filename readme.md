# Car Image Card – Django CRUD App

A **simple but complete Django CRUD application** to manage car image cards. The app allows users to **upload, view, update, and delete car data** along with images. No magic, no shortcuts — just clean Django fundamentals.

---

## 🚗 Features

* Upload car details with image
* Display cars as image cards
* Update existing car data and image
* Delete car records
* Media file handling using Django
* Clean, minimal UI (template-based)

---

## 🛠 Tech Stack

* **Backend:** Django
* **Database:** SQLite (default, can be swapped)
* **Frontend:** HTML, CSS (Django Templates)
* **Image Handling:** Django Media Files

---

## 📁 Project Structure

```
ImgCard/
│
├── ImgCard/        # Project settings
│
├── App1/               # Main app
│   ├── migrations/
│   ├── templates/
│   │   └── App1/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── media/              # Uploaded images
├── staticfiles/        # Collected static files
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <repo-url>
cd ImgCard
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Open browser and visit:

```
http://127.0.0.1:8000/
```
---

## 🔄 CRUD Operations

| Operation | Description                 |
| --------- | --------------------------- |
| Create    | Upload new car with image   |
| Read      | Display cars as image cards |
| Update    | Edit car details & image    |
| Delete    | Remove car entry            |

---

## 🖼 Media Configuration

Make sure this exists in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

And in `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---