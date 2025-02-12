# Social Book

Social Book is a Django-based web application that allows users to register, log in, upload books, and interact with a user-friendly dashboard. The project also integrates GitHub, Django authentication, CSS templates, and API functionalities.

## Features

- User Registration and Login System
- Custom User Model replacing Django's default authentication model
- Dashboard to view all registered users
- File Upload Mechanism for Books (PDF, JPEG formats)
- Integration with Django Libraries: Djoser, Django REST Framework, SQLAlchemy
- Data Transformation using Pandas and NumPy
- API to login and fetch uploaded files
- Two-Step Authentication
- Email Notification on Login

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/social_book.git
cd social_book
```

### 2. Set Up a Virtual Environment
```bash
python -m venv env
source env/bin/activate   # For macOS/Linux
env\Scripts\activate    # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File for SMTP Configuration
To enable email notifications, create a `.env` file in the same directory as `manage.py` and add the following:

```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-digit-app-password
```

> **Note:** You need to enable 2FA for your Google account and generate an app password.

### 5. Apply Migrations and Run the Server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 6. Access the Application
Open your browser and go to:  
`http://127.0.0.1:8000/`

## Usage

- **Register an account** on the platform.
- **Log in** to access the dashboard.
- **Upload Books** from the dashboard.
- **View Uploaded Files** in "My Books" section.
- **Public Visibility** feature allows users to choose whether their profile is visible.

## API Endpoints

1. **Login and Get Token**
   ```http
   POST /api/auth/token/login/
   ```

2. **Fetch Uploaded Files (Authenticated Users)**
   ```http
   GET /api/user/files/
   ```

## Technologies Used

- **Django** - Web framework
- **Django REST Framework** - API development
- **Djoser** - Authentication system
- **SQLAlchemy** - Database interaction
- **Pandas & NumPy** - Data wrangling
- **Bootstrap/CSS** - Frontend styling

## License
This project is open-source and available for educational and personal use.
