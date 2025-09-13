# Django Blog Project

A comprehensive blog application built with Django 5.1 that allows for complete content and user management, including categories, posts, advertisements, and user profiles. This project is designed for educational purposes or as a foundation for a fully functional blog platform.

## Features

* **User Management:**

  * Registration, login, logout
  * Profile editing (username and email)
  * Role-based permissions: only users in the 'Authors' group can create posts

* **Post Management:**

  * Create, edit, delete, and view posts
  * Rich text editor with CKEditor for content
  * Assign posts to categories
  * Upload thumbnail images for posts
  * Automatic calculation of content length

* **Category Management:**

  * Create categories with optional parent-child relationships
  * Add thumbnail images for categories
  * Ordering of categories

* **Advertisement System:**

  * Display banners with links on different pages
  * Optional expiration dates for advertisements

* **Media and Static Files:**

  * Upload and serve media files (images)
  * Manage static files like CSS and JavaScript

* **Analytics:**

  * Track total characters written by each user across all posts

* **Pagination:**

  * Display posts in a paginated view (10 posts per page by default)

## Requirements

* Python 3.10+
* Django 5.1.3
* Pillow (for image handling)
* django-ckeditor (for rich text editing)
* beautifulsoup4 (for content parsing and analytics)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <project_folder>
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3. Configure settings in `settings.py`:

   * Set `SECRET_KEY` (keep it secret in production)
   * Set `DEBUG = True` for development
   * Configure `ALLOWED_HOSTS` for production deployment

## Database Setup

1. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

Start the development server:

```bash
python manage.py runserver
```

* Access the project at `http://127.0.0.1:8000/`
* Uploaded media files are stored in the `media/` directory

## Project Structure

```
project/
│
├── blog/
│   ├── admin.py            # Register models in admin panel
│   ├── apps.py             # Application configuration
│   ├── forms.py            # Post and profile forms
│   ├── models.py           # Database models: Post, Category, Advertisement, UserProfile
│   ├── urls.py             # App-level URL routing
│   ├── views.py            # Views for posts, categories, users, and ads
│   └── ...                 # Other app files
│
├── project/
│   ├── settings.py         # Main project settings
│   ├── urls.py             # Project-level URL routing
│   └── wsgi.py             # WSGI entry point
│
├── static/                 # Static files (CSS, JS, images)
├── media/                  # Media files uploaded by users
├── db.sqlite3              # SQLite database (default)
└── manage.py               # Django management commands
```

## Models Overview

* **Category:** Represents post categories with optional parent, thumbnail image, and order
* **Post:** Main content model with title, rich content, author, category, thumbnail, and timestamps
* **Advertisement:** Holds banners for pages with link and optional expiration date
* **UserProfile:** Extends user model to track total content characters

## Forms Overview

* **PostForm:** Handles creation and editing of posts with CKEditor widget
* **ProfileEditForm:** Allows users to update username and email

## Views Overview

* **Posts:** List, detail, create (authors only), and delete
* **Categories:** Display posts by category
* **Users:** Registration, login, logout, profile display, and editing
* **Advertisements:** Display ads on specific pages
* **Authorization:** Ensure only authorized users can create or edit content

## Deployment Notes

* For production, set `DEBUG = False` and configure `ALLOWED_HOSTS`
* Use a production-ready database such as PostgreSQL
* Serve static and media files with a web server like Nginx
* Secure `SECRET_KEY` and sensitive information

## License

This project is licensed under the MIT License. 
