
# Bug Tracking Dashboard

## Project Overview

The **Bug Tracking Dashboard** is a web application built with **Django** to help users manage and track bugs. The dashboard allows users to log bugs, view detailed analytics, filter bug reports, and visualize bug trends. It features a simple and intuitive interface with various pages, such as bug management, analytics, and uploading bulk data.

### Features
- **Bug Management**: Users can add, edit, and delete bug reports.
- **Analytics**: Visualize bug trends and statistics.
- **CSV Data Upload**: Admins can upload bug data in bulk through CSV files.
- **Data Visualization**: Includes visualizations like pie charts and bar charts for bug analysis.

### Technologies Used
- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS, JavaScript
- **Data Visualization**: Matplotlib, Plotly
- **Database**: SQLite (or PostgreSQL/MySQL, depending on setup)
- **File Upload**: CSV for bulk data entry

## Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/teja-techenthusiast/djanjo-projects
   ```

2. **Navigate to the Project Directory**:
   ```
   cd bug-tracking-dashboard
   ```

3. **Set Up a Virtual Environment**:
   ```
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. **Install Required Dependencies**:
   ```
   pip install -r requirements.txt
   ```

6. **Run Database Migrations**:
   ```
   python manage.py migrate
   ```

7. **Create a Superuser (Optional)**:
   If you want to access the Django admin dashboard:
   ```
   python manage.py createsuperuser
   ```

8. **Start the Development Server**:
   ```
   python manage.py runserver
   ```

9. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:8000/`.

## Folder Structure

```
bug-tracking-dashboard/
├── bug_tracker/              # Django app containing core functionality
│   ├── migrations/           # Database migration files
│   │   └── 0001_initial.py   # Initial database migrations
│   ├── templates/            # HTML templates for frontend
│   │   ├── dashboard/        # Template folder for dashboard views
│   │   │   ├── add_bug.html  # Page for adding new bugs
│   │   │   ├── analytics.html # Page showing bug analytics
│   │   │   ├── base.html     # Base template for consistent layout
│   │   │   ├── bug_list.html # Page for listing all bugs
│   │   │   └── home.html     # Homepage view
│   ├── static/               # Static files like CSS, JS
│   │   ├── styles.css        # CSS file for styling the dashboard
│   ├── upload_data.html      # Template for uploading CSV data
│── models.py             # Bug models and other app-related models
│── views.py              # Views for rendering pages (home, bug list, etc.)
│── admin.py              # Django admin configuration for bug models
│── apps.py               # Django app configuration
│── forms.py              # Forms for handling bug data entry
│── tests.py              # Unit tests for bug tracker functionality
│   ├── urls.py               # URL routing for bug tracker app
├── requirements.txt          # List of Python dependencies
├── manage.py                 # Django management script
├── README.md                 # This file
└── db.sqlite3                # SQLite database file (or another DB)
```

## How to Contribute

Feel free to fork the repository, submit pull requests, or report issues. Here are some ways you can contribute:
- Reporting bugs or suggesting improvements
- Improving the UI/UX design
- Enhancing data visualization features

